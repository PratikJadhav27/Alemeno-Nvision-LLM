from google import genai
from google.genai import types
import os
import time
from pathlib import Path
from dotenv import load_dotenv
import csv
import mimetypes

# --- Configuration ---
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
if not API_KEY:
    raise ValueError("GENAI_API_KEY not found in environment variables or .env file.")

# Initialize the Gemini API client
client = genai.Client(api_key=API_KEY)

# --- Constants ---
REFERENCE_IMAGE_DIR = Path("reference_images")
NORMAL_IMAGE_DIR = REFERENCE_IMAGE_DIR / "normal"
DEFECT_IMAGE_DIR = REFERENCE_IMAGE_DIR / "defect_images"
TEST_IMAGE_DIR = Path("test_images")
EXPECTED_NORMAL_IMAGES = 1
EXPECTED_DEFECT_IMAGES = 4
DETAILS_CSV_PATH = Path("evaluation_details.csv")
ACCURACY_OUTPUT_PATH = Path("accuracy_results.txt")
MODEL_NAME = "gemini-2.0-flash"

try:
    from defect_prompts import DEFECT_PROMPTS
except ImportError:
    raise ImportError("Could not import DEFECT_PROMPTS from defect_prompts.py.")

TARGET_DEFECT = "White Patches"

def get_mime_type(file_path):
    """Get MIME type based on file extension."""
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or "application/octet-stream"

def upload_reference_images():
    """Upload reference images and return file objects."""
    # Normal image (no defects)
    normal_images = [f for f in NORMAL_IMAGE_DIR.iterdir() 
                   if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg']]
    
    if not normal_images:
        raise FileNotFoundError(f"No normal images found in {NORMAL_IMAGE_DIR}")
    if len(normal_images) < EXPECTED_NORMAL_IMAGES:
        raise FileNotFoundError(f"Need at least {EXPECTED_NORMAL_IMAGES} normal image, found {len(normal_images)}")
    
    # Upload normal image
    normal_file = client.files.upload(file=str(normal_images[0]))
    
    # Defect images
    defect_images = [f for f in DEFECT_IMAGE_DIR.iterdir() 
                   if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg']]
    
    if len(defect_images) < EXPECTED_DEFECT_IMAGES:
        raise FileNotFoundError(f"Need at least {EXPECTED_DEFECT_IMAGES} defect images, found {len(defect_images)} in {DEFECT_IMAGE_DIR}")
    
    defect_files = []
    for img_path in defect_images[:EXPECTED_DEFECT_IMAGES]:
        defect_files.append(client.files.upload(file=str(img_path)))
    
    return normal_file, defect_files

def check_defect(normal_file, defect_files, test_image_path):
    """Analyzes image for the target defect, returns Yes/No/Error."""
    defect_description = DEFECT_PROMPTS.get(TARGET_DEFECT, "")
    if not defect_description:
        return "Error"
    
    try:
        # Build contents list
        contents = [
            defect_description,
            "\n\n--- Context Images ---",
            "\nImage 'image_1_normal.png' is an image of a display panel that has no defects:",
            normal_file,
            f"\nImages 'image_2.png', 'image_3.png', 'image_4.png' and 'image_5.png' are images of display panels that have {TARGET_DEFECT} defect:"
        ]
        
        # Add defect images
        contents.extend(defect_files)
        
        # Add test image
        test_file = client.files.upload(file=str(test_image_path))
        contents.extend([
            "\n\n--- Test Image ---",
            "This is the test image:",
            test_file,
            f"\n\n--- Instruction ---\nBased on the defect description and context images, does the test image have {TARGET_DEFECT} defect? Reply in one word Yes or No."
        ])
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=contents
                )
                result_text = response.text.strip().lower()
                if 'yes' in result_text and 'no' not in result_text:
                    return "Yes"
                if 'no' in result_text and 'yes' not in result_text:
                    return "No"
                return "No"  # Default to No if unclear
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(5 * (2 ** attempt))  # Exponential backoff
                else:
                    print(f"Error processing {test_image_path.name}: {str(e)}")
                    return "Error"
        return "Error"
    except Exception as e:
        print(f"Critical error with {test_image_path.name}: {str(e)}")
        return "Error"

def initialize_csv(filepath: Path, headers: list):
    if not filepath.is_file():
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(headers)

def append_to_details_csv(filepath: Path, data_row: list):
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(data_row)

def save_accuracy_results(metrics):
    """Save accuracy results to a text file."""
    with open(ACCURACY_OUTPUT_PATH, 'w') as f:
        f.write("=== Accuracy Results ===\n\n")
        f.write(f"Defect: {TARGET_DEFECT}\n")
        f.write(f"Total Test Images: {metrics['total']}\n")
        f.write(f"Defect Images: {metrics['expected_defect']}\n")
        f.write(f"Non-Defect Images: {metrics['expected_no_defect']}\n")
        f.write(f"Predicted Defect: {metrics['predicted_defect']}\n")
        f.write(f"Predicted No Defect: {metrics['predicted_no_defect']}\n")
        f.write(f"True Positives: {metrics['tp']}\n")
        f.write(f"True Negatives: {metrics['tn']}\n")
        f.write(f"False Positives: {metrics['fp']}\n")
        f.write(f"False Negatives: {metrics['fn']}\n")
        f.write(f"Accuracy: {metrics['accuracy']}%\n")
        f.write(f"\nProcessed Images: {metrics['processed']}\n")
        f.write(f"Errors: {metrics['errors']}\n")

def calculate_metrics(results):
    """Calculate evaluation metrics from results."""
    metrics = {
        'total': len(results),
        'expected_defect': 0,
        'expected_no_defect': 0,
        'tp': 0,  # True Positives
        'tn': 0,  # True Negatives
        'fp': 0,  # False Positives
        'fn': 0,  # False Negatives
        'predicted_defect': 0,
        'predicted_no_defect': 0,
    }
    
    for expected, predicted in results:
        if expected == "defect":
            metrics['expected_defect'] += 1
        else:
            metrics['expected_no_defect'] += 1
            
        if predicted == "Yes":
            metrics['predicted_defect'] += 1
        else:
            metrics['predicted_no_defect'] += 1
            
        if expected == "defect":
            if predicted == "Yes":
                metrics['tp'] += 1
            else:
                metrics['fn'] += 1
        else:
            if predicted == "No":
                metrics['tn'] += 1
            else:
                metrics['fp'] += 1
    
    correct = metrics['tp'] + metrics['tn']
    metrics['accuracy'] = int((correct / metrics['total']) * 100) if metrics['total'] > 0 else 0
    
    return metrics

def run_evaluation():
    print(f"Starting evaluation for defect: {TARGET_DEFECT}")
    start_time_total = time.time()

    initialize_csv(DETAILS_CSV_PATH, ['image_path', 'expected', 'predicted', 'is_correct', 'status'])

    DEFECT_TEST_DIR = TEST_IMAGE_DIR / "defect"
    NO_DEFECT_TEST_DIR = TEST_IMAGE_DIR / "no_defect"
    
    if not DEFECT_TEST_DIR.is_dir():
        print(f"Error: Defect test image directory not found: '{DEFECT_TEST_DIR}'.")
        return
    if not NO_DEFECT_TEST_DIR.is_dir():
        print(f"Error: Non-defect test image directory not found: '{NO_DEFECT_TEST_DIR}'.")
        return

    test_cases = []
    for img_path in DEFECT_TEST_DIR.iterdir():
        if img_path.is_file() and img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            test_cases.append((img_path, "defect"))
    
    for img_path in NO_DEFECT_TEST_DIR.iterdir():
        if img_path.is_file() and img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            test_cases.append((img_path, "no_defect"))
    
    if not test_cases:
        print(f"Error: No test images found in {TEST_IMAGE_DIR}")
        return

    print(f"Found {len(test_cases)} test images")

    try:
        print("Loading reference images...")
        normal_file, defect_files = upload_reference_images()
        print(f"Loaded: 1 normal image and {len(defect_files)} defect images")
    except Exception as e:
        print(f"Error loading reference images: {str(e)}")
        return

    results = []
    processed_count = 0

    for index, (test_image_path, expected) in enumerate(test_cases):
        print(f"\nProcessing [{index+1}/{len(test_cases)}]: {test_image_path.name} (Expected: {expected})")
        
        result = check_defect(normal_file, defect_files, test_image_path)
        if result == "Error":
            print(f"  Error: Analysis failed. Skipping.")
            status = 'Analysis Error'
            predicted = "No" if expected == "defect" else "Yes"
        else:
            processed_count += 1
            predicted = result
            if (expected == "defect" and predicted == "Yes") or (expected == "no_defect" and predicted == "No"):
                status = 'Correct'
                is_correct = True
            else:
                status = 'Incorrect'
                is_correct = False
        
        results.append((expected, predicted))
        
        append_to_details_csv(DETAILS_CSV_PATH, [
            test_image_path.relative_to(TEST_IMAGE_DIR),
            expected,
            predicted,
            is_correct if 'is_correct' in locals() else False,
            status
        ])

    metrics = calculate_metrics(results)
    metrics['processed'] = processed_count
    metrics['errors'] = len(test_cases) - processed_count

    print(f"\n=== Evaluation Summary ===")
    print(f"Total Test Images: {metrics['total']}")
    print(f"Accuracy: {metrics['accuracy']}%")

    save_accuracy_results(metrics)
    
    print(f"\nTotal Evaluation Time: {time.time() - start_time_total:.2f} seconds")

if __name__ == "__main__":
    if not TEST_IMAGE_DIR.is_dir():
        print(f"Error: Test image directory not found: '{TEST_IMAGE_DIR}'.")
    elif not NORMAL_IMAGE_DIR.is_dir():
        print(f"Error: Normal image directory not found: '{NORMAL_IMAGE_DIR}'.")
    elif not DEFECT_IMAGE_DIR.is_dir():
        print(f"Error: Defect image directory not found: '{DEFECT_IMAGE_DIR}'.")
    else:
        run_evaluation()