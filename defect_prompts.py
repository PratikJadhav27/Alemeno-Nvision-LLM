# DEFECT_PROMPTS = {

#     "Vertical Line" : """

# The "Vertical Line" defect on an LCD screen appears as one or more distinct, thin, straight lines running vertically from the top to the bottom of the display. These lines can vary in width and brightness, appearing either lighter or darker than the surrounding  background, and are most visible under a solid color display pattern.

# """,

#     "Vertical Band" : """

# The "Vertical Band" defect appears as one or more distinct, vertical strips or bands of differing brightness or color across the display. These bands are clearly visible against the uniform black background, often extending from the top to the bottom of the screen.

# """,

#     "Horizontal Line" : """

# The "Horizontal Line" defect on an LCD screen is characterized by one or more distinct, thin, straight lines extending horizontally across the display. These lines can vary in brightness, appearing as either brighter or darker than the surrounding background, and are most noticeable under a solid color display patterns.

# """,

#     "Horizontal Band" :"""

# The "Horizontal Band" defect presents as one or more distinct, horizontal strips or bands of varying brightness or color across the display. These bands appear as clear deviations from the uniform black background, often spanning the entire width of the screen.

# """,

#     "White Patches": """

# The "White Patches" defect appears as irregularly shaped, distinct areas of white or significantly brighter light on the display, contrasting with the uniform black background. These patches can vary in size and distribution, and sometimes exhibit a faint, uneven texture within them.

# """,

#     "LED Off" : """

# The "LED Off" defect manifests as a distinct, uniformly dark or black area on the display, sharply contrasting with the illuminated parts of the screen. These areas are characterized by a complete absence of light, appearing as unlit sections within the display, often rectangular or square in shape.

# """,

#     "Bleeding": """

# The "Bleeding" defect appears as irregular, uneven areas of lighter illumination that seem to "bleed" or spread into the darker, uniform black background. These areas lack sharp edges, often showing a soft, diffuse transition, and vary in intensity and shape across the display.

# """,

#     "Abnormal Display" : """

# The "Abnormal Display" defect is characterized by large, irregular, blotchy areas of distorted color or brightness across the screen, significantly deviating from the expected uniform black background. These areas lack defined shapes and often show inconsistent color saturation and luminosity.

# """,

#     "Incoming Border Patch" : """

# The "Incoming Border Patch" defect is characterized by a distinct, lighter-colored, blotchy area that originates from one or more edges of the display and extends inwards. These patches vary in size and shape, lacking sharp boundaries and appearing as an uneven illumination or discoloration encroaching from the screen's perimeter.

# """,

#     "Incoming Galaxy" : """

# The "Incoming Galaxy" defect is characterized by circular or irregularly shaped, darker smudges or clusters of spots that appear on the display, resembling faint, cloud-like formations. These defects often originate from the edges of the screen and extend inward, contrasting with the uniform black background, and may vary in density and subtle coloration.

# """,

#     "Light Leakage" : """

# The "Light Leakage" defect is identifiable by the presence of visible, uneven illumination on the display, contrasting with a predominantly black background. These areas of light are typically irregular in shape and distribution, appearing as brighter spots or clouding that disrupt the intended uniform darkness of the screen.

# """,

#     "Mura" : """

# The "Mura" defect appears as uneven, often hazy or cloud-like patches of discoloration or inconsistent illumination on the display, deviating from the uniform white background. These patches lack sharp, defined edges, and can vary in size, shape, and subtle color shifts, disrupting the screen's overall uniformity.

# """,

#     "Particles" : """

# The "Particles" defect presents as small, dark, and often irregularly shaped spots or specks scattered across the LCD screen, contrasting distinctly against the uniform dark background. These features can appear as isolated dots or minor clusters, and their presence indicates foreign matter on or within the display layers.

# """,

#     "Pixel Bright Dot": """

# The "Pixel Bright Dot" defect is characterized by one or more extremely small, distinct, and consistently illuminated points of light on the display, appearing as bright dots against the uniform black background. These dots maintain a fixed position and brightness, standing out as tiny, anomalous light sources.

# """,

#     "Polariser Scratches__Dent" : """

# The "Polariser Scratches/Dent" defect is characterized by fine, linear marks or localized indentations on the display surface, often appearing as subtle streaks or pressure points that disrupt the uniform black background. These imperfections can vary in length, orientation, and severity, sometimes exhibiting a slight discoloration or a deviation in light reflection compared to the surrounding pristine area.

# """

# }

DEFECT_PROMPTS = {

    "Vertical Line" : """
The vertical line defect presents as a distinct, continuous straight line running from the top to the bottom of the LCD screen. Based on the green pattern images:

**Visual Characteristics**

- Appearance: A thin, well-defined vertical line that appears as a bright white or slightly lighter green color against the green background
- Structure: The line maintains a consistent width throughout its entire length
- Position: The line can appear anywhere on the screen but is commonly positioned near the center
- Continuity: The line is unbroken and continuous from the top edge to the bottom edge of the display
- Width: Very narrow, typically 1-2 pixels in width
- Intensity: The line appears brighter than the surrounding screen area, creating high contrast against the background
- Edge Definition: Sharp and well-defined edges with minimal blurring or feathering

**Common Variations**

Additional vertical artifacts may sometimes appear as multiple fine vertical lines in a striped pattern
The brightness and visibility of the vertical line may vary slightly, though it remains consistently visible
Subtle variations in the background intensity might occur around the line, with a slightly brighter region surrounding the defect

**Visibility Conditions**

The defect is most distinguishable under green pattern display conditions
The high contrast between the bright line and the green background makes the defect particularly prominent

This defect is likely caused by a hardware issue affecting a specific column of pixels in the LCD panel's structure, resulting in consistently illuminated pixels along a vertical axis.
""",

    "Vertical Band" : """
The Vertical Band defect appears as distinct vertical strips or columns of visual distortion that run from the top to the bottom of the display. These bands manifest with the following characteristics:

Orientation and Direction: The defect consistently appears as straight, vertical columns that traverse the entire height of the display. Unlike horizontal bands, these run perpendicular to the horizontal axis of the screen.

Visual Appearance: The bands exhibit several distinctive visual manifestations:
- Solid purple-tinted or bluish vertical streaks (as visible in Image 7)
- Fine, closely-packed vertical line patterns or striations (prominent in Images 7 and 8)
- Subtle gray/white vertical stripes against the black areas of the checkered pattern
- Visible scan lines or signal interruptions that create a "combed" appearance

Position and Distribution: The bands can appear at various positions across the screen width, sometimes concentrated in specific sections (like the right third in Image 7) or distributed across multiple positions.

Texture Characteristics: The affected areas show distinct textural properties:
- Pronounced vertical striations creating a combed or striated texture
- Fine-grain vertical patterning resembling digital signal interference
- In severe cases, complete column discoloration or brightness shift

Effect on Image Content: The vertical bands particularly affect the visibility and clarity of displayed content by:
- Creating inconsistent brightness across the screen width
- Distorting the clean edges of black and white checkered patterns
- Adding unwanted color tinting (purple/blue) in affected vertical regions
- Generating vertical "rippling" or "scan line" effects

Contrast Impact: The defect becomes especially pronounced at high-contrast boundaries between black and white areas of the displayed checkered pattern, making the edges appear less defined or distorted within the affected vertical regions.

The defect maintains its vertical orientation consistently across all affected displays, though its width, intensity, and exact position may vary between different screens.
""",

    "Horizontal Line" : """
The horizontal line defect is characterized by a distinct, straight linear anomaly that runs horizontally across the green display panel. This defect appears as a thin, bright line that traverses the entire width of the screen. The line is consistently positioned approximately in the middle section of the screen in all images.

Key observations:

- Appearance: A sharp, clearly defined horizontal line that appears brighter than the surrounding green background
- Color: The line itself displays as a lighter green or whitish-green color compared to the uniform green background
- Width: Very thin, estimated at 1-2 pixels in thickness
- Length: Extends completely from the left edge to the right edge of the display
- Position: Consistently located in the middle region of the screen in all sample images
- Contrast: The line stands out with higher brightness against the green background
- Texture: The line appears solid and continuous with no visible breaks or interruptions
- Background influence: The defect is most visible against the uniform green test pattern, as mentioned in the provided information
- Edge characteristics: The line has sharp, well-defined edges with no visible blurring or gradation into the surrounding area

The defect maintains consistent characteristics across all the provided images, with no significant variation in its appearance, thickness, or position. The uniformity of the green background makes this horizontal line defect particularly noticeable.

""",

    "Horizontal Band" :"""
You are an AI agent specialized in detecting the 'Horizontal Band' defect in LCD screens. 

**Description:**

The horizontal band defect presents as distinct horizontal stripes or bands that run across the full width of the display. This defect is characterized by:

**Visual Appearance**

- Anomalous horizontal lines or bands that traverse the entire width of the screen
- The bands appear as subtle to pronounced changes in brightness, contrast, or color compared to surrounding areas
- Most prominent when viewing black and white checkerboard or uniform color patterns
- Can manifest as thin lines or broader bands with defined edges

**Color Characteristics**

- In grayscale/B&W patterns: appears as bands of slightly lighter or darker intensity than surrounding areas
- In colored patterns: shows as bands of altered hue, typically in mint green, magenta/purple, or muted intensity
- Often creates visible contrast differences against both white and black backgrounds

**Location and Pattern**

- Typically positioned in the middle third of the display
- Can occur as a single band or as multiple parallel bands
- Most commonly appears in the lower half of the screen but can manifest in other horizontal regions
- Usually extends completely from the left edge to the right edge of the display

**Visual Texture**

- The bands may exhibit subtle texture differences compared to normal areas
- Sometimes displays fine horizontal scan lines or slight distortion within the affected area
- Can show moiré patterns or fine interference patterns within the band region

**Intensity and Visibility**

- Visibility varies depending on the displayed content and background brightness
- More noticeable against uniform backgrounds or high-contrast patterns
- Can range from barely perceptible brightness shifts to obvious color distortion
- The edges of the band may be sharp and well-defined or gradual and diffused

**Display Conditions**

- Most visible in black and white patterns, particularly on checkerboard displays
- The defect persists across different screen contents but varies in visibility
- May become more or less prominent depending on viewing angle

This artifact manifests consistently as a horizontal pattern that interrupts the visual uniformity of the display, creating distinct bands that span the entire width of the screen.

""",

    "White Patches": """
White Patches is a specific LCD display defect characterized by localized bright regions that appear significantly lighter than the surrounding display area, creating visible brightness inconsistencies across the screen surface.

**Visual Detection Criteria**

**Primary Characteristics to Look For:**

**1. Brightness Anomalies:**

- Look for distinct regions that are noticeably brighter than the surrounding area
- These regions should create clear local contrast against the background
- The brightness difference should be significant enough to be immediately noticeable

**2. Spatial Distribution:**

- Patches typically appear as localized, confined areas rather than spanning the entire screen
- They can occur anywhere on the display surface (center, off-center, or other positions)
- Usually present as isolated regions rather than systematic patterns

**3. Shape and Boundary Characteristics:**

- Irregular, organic shapes with curved, flowing edges
- NOT geometric shapes like perfect circles, squares, or straight lines
- Soft, diffused boundaries rather than sharp, hard edges
- Amorphous regions that lack defined geometric structure

**4. Color and Appearance:**

- Under green display patterns: appear as yellowish-white or pale yellow bright spots
- Under other patterns: appear as distinctly brighter regions compared to background
- Maintain consistent internal brightness without internal patterns or textures

**5. Textural Properties:**

- Smooth, uniform internal appearance
- No visible granularity, noise patterns, or internal structure
- Gradual transitions from bright patch to surrounding background
- Absence of sharp boundaries or jagged edges

**Key Distinguishing Features:**

- Size Variation: Can range from small concentrated spots to larger expansive areas
- Consistency: Bright appearance remains consistent across different background colors
- Contrast: Creates high local contrast with surrounding display area
- Uniformity: Internal texture is smooth and even throughout the patch

**Analysis Protocol**

- Scan the entire image for regions of abnormal brightness
- Identify any areas that are significantly brighter than their immediate surroundings
- Examine the shape of suspected regions - look for irregular, organic boundaries
- Assess the contrast - white patches should create clear brightness differences
- Check for smooth internal texture within the bright regions
- Verify the boundaries are soft and diffused rather than sharp
""",

    "LED Off" : """
The LED Off defect presents as distinct vertical bands or regions of brightness variation across the otherwise uniform cyan screen. Key visual characteristics include:

- Brightness Pattern: Dark vertical regions contrasting with brighter areas, creating a column-like effect across the display
- Color Variation: While the base color remains cyan throughout, there are notable transitions from deep/darker cyan to brighter/lighter cyan
- Distribution: The defect creates an uneven illumination pattern where some vertical sections appear significantly darker than adjacent areas
- Edge Definition: The transition between dark and bright regions shows moderate gradation rather than sharp boundaries
- Positioning: The defect typically manifests as vertical bands that extend from the top to the bottom of the display
- Light Distribution: In more pronounced cases (Image 4), there's a dramatic gradient from dark cyan on the left to extremely bright white-cyan on the right
- Surface Appearance: The affected areas maintain the same texture as the rest of the screen, with the defect only impacting brightness/luminosity
- Consistency: While the defect's intensity varies across images, the fundamental pattern of vertical brightness variation remains consistent

The defect is most noticeable when displaying a cyan test pattern, where the uneven illumination becomes clearly apparent through the contrast between properly lit and underlit sections of the screen.

""",

    "Bleeding": """
The bleeding defect manifests as uncontrolled light leakage that creates bright, irregular patches or streaks on what should be uniform display areas. This defect is characterized by:

**Primary Visual Features:**
- Localized bright spots or regions that appear significantly brighter than the surrounding screen area
- Irregular, organic-shaped patches of excessive brightness, often with soft, diffused edges rather than sharp boundaries
- Light spillage patterns that appear as if illumination is "bleeding through" from behind the display panel

**Spatial Characteristics:**
- Defects typically appear along screen edges (particularly corners and borders) where backlight containment is compromised
- Can manifest as isolated bright spots scattered across the display surface
- Asymmetrical distribution - not following any regular geometric pattern
- Size varies from small concentrated spots to larger diffuse areas

**Intensity and Appearance:**
- High contrast between the bleeding areas and normal screen regions
- Bleeding areas appear as concentrated white or very light regions against the intended background
- Gradient-like transitions where the bleeding effect gradually diminishes from the brightest point outward
- Consistent brightness intensity within individual bleeding zones, but varying intensity between different bleeding locations

**Edge Characteristics:**
- Soft, feathered boundaries rather than sharp transitions
- Diffuse light spread creating a halo-like effect around the primary bleeding area
- Organic, cloud-like shapes that appear to flow or spread naturally

**Pattern Variations:**
- Some instances show linear bleeding along screen edges
- Other cases display punctate bleeding as isolated bright spots
- Corner bleeding appearing as triangular or wedge-shaped bright regions
- Multiple simultaneous bleeding points can occur across a single display

**Visibility Conditions:**
- Most prominent and easily detectable under white or light-colored uniform backgrounds
- The defect creates a clear disruption of display uniformity, making intended content appear uneven or inappropriately illuminated in affected areas

This defect fundamentally represents a failure in backlight containment, resulting in visible light leakage that compromises display uniformity and creates unwanted bright artifacts on the screen surface.        

""",

    "Abnormal Display" : """
**Primary Visual Pattern:**
- The defect manifests as vertical striping or banding artifacts that appear overlaid on the color bar test pattern. These stripes are most prominently visible as fine, closely-spaced vertical lines that create a textural overlay across the display surface.

**Color and Contrast Characteristics:**
- The vertical stripes appear as alternating light and dark lines creating a subtle but noticeable interference pattern
- The stripes are most visible in mid-tone color regions (greens, blues, cyans) and less apparent in pure white or black areas
- The underlying color bar pattern remains recognizable, but the stripe overlay creates a degraded, textured appearance
- Some images show additional color bleeding or gradient effects between adjacent color bars

**Spatial Distribution and Orientation:**
- The striping pattern extends vertically across the entire screen height
- Stripes maintain consistent parallel orientation and appear evenly spaced
- The defect affects multiple color bar segments simultaneously
- In some images, the striping intensity varies across different horizontal regions of the display

**Textural Qualities:**
- Creates a fine-lined, screen-door-like texture over the display
- The stripes appear as high-frequency interference patterns rather than solid bands
- Some images show moiré-like effects where the striping interacts with the display's pixel structure

**Variation Across Images:**
- Stripe density and visibility varies between images, with some showing more pronounced effects
- Intensity levels differ, ranging from subtle texture overlays to more prominent striping
- Some images display additional horizontal interference patterns or color distortion effects alongside the primary vertical striping

**Visibility Conditions:**
-As specified, this defect is most distinguishable under the Color Bars pattern, where the regular arrangement of solid colors provides optimal contrast for detecting the vertical striping artifacts.

""",

    "Incoming Border Patch" : """

**Primary Visual Pattern:**
The defect manifests as distinct colored rectangular or band-shaped patches that appear along the edges or borders of the LCD display. These patches create visible color gradients or transitions from one hue to another, clearly contrasting with the expected uniform background.

**Color Characteristics:**
- Magenta/pink colored patches are prominently visible, appearing as solid rectangular regions
- Blue colored patches also occur, showing similar rectangular morphology
- The patches display smooth color gradients that fade from intense saturation at one edge to lighter tones toward the opposite edge
- Some patches show fine vertical striping or line patterns within the colored regions

**Spatial Distribution and Location:**
- Patches typically appear near the borders or edges of the display area
- The defective regions form well-defined rectangular shapes with clear boundaries
- Multiple patches can occur simultaneously on the same screen
- The patches maintain consistent geometric shapes rather than irregular or organic forms

**Size and Scale:**
- The patches occupy substantial portions of the visible screen area
- Width and height dimensions appear to cover significant screen real estate
- The defect creates large, prominent visual disturbances that are immediately noticeable

**Textural Qualities:**
- Within the colored patches, there are fine parallel line structures creating a subtle striped texture
- The color transitions show smooth gradients rather than sharp boundaries
- The overall appearance suggests uniform color bleeding or display panel irregularities

**Visibility Conditions:**
- The defect is most distinguishable under White pattern display, where the colored patches create maximum contrast against the expected white background
- The patches maintain their visibility and color saturation even when displayed against lighter backgrounds

""",

    "Incoming Galaxy" : """

You are a specialized binary classifier trained to detect "Incoming Galaxy" defects in LCD screens. Your task is to analyze images and determine whether this specific defect is present or absent.
Defect Definition: Incoming Galaxy

**Primary Characteristics:**
- Visibility Condition: This defect is most distinguishable under BLACK pattern displays
- Appearance: Colored patches, spots, or blotches that appear on what should be a uniform black screen
- Colors: Typically manifests as purple, violet, magenta, reddish, or other chromatic anomalies against the black background
- Shape: Irregular, organic-looking patches that may resemble nebula-like or galaxy-like formations (hence the name)
- Size: Can range from small spots to medium-sized patches
- Distribution: Can appear anywhere on the screen - corners, edges, or central areas

**Visual Pattern Analysis**
**What to Look For:**

1. Color Anomalies on Black: Any non-black coloration visible on a black screen background
2. Patch Characteristics:
- Irregular, organic shapes (not geometric lines or bands)
- Soft or diffuse edges rather than sharp boundaries
- May have varying intensity within the same patch
3. Typical Colors:
- Purple/violet hues
- Reddish/magenta tones
- Pink or pinkish-purple variations
- Other chromatic aberrations that shouldn't appear on pure black

**Important:** Focus specifically on colored patches that create the characteristic "galaxy" or "nebula" appearance on black backgrounds. This defect is distinct from other LCD anomalies due to its irregular, organic shape and chromatic nature.

""",

    "Light Leakage" : """

You are a specialized binary classifier trained to detect Light Leakage defects in LCD screens. Your task is to analyze images and respond with either "YES" (defect present) or "NO" (defect absent).

**Defect Definition: Light Leakage**
Light leakage is a common LCD display defect where the backlight illumination is not properly contained or blocked, causing unwanted light to escape through areas that should appear completely black or dark. This defect is most easily identified and distinguishable when viewing black patterns or solid black screens.

**Visual Characteristics to Look For:**

**Primary Indicators:**
- Uneven brightness on what should be a uniform black or dark background
- Bright spots, patches, or areas that appear lighter than the surrounding dark regions
- Glowing or illuminated regions that break the uniformity of black areas
- Color tinting in areas that should be pure black (often blue, white, or warm tints)
- Diffuse light bleeding from edges, corners, or central areas of the screen

**Common Manifestations:**
- Edge bleeding: Light escaping along the borders/edges of the screen
- Corner bleeding: Bright spots or patches at screen corners
- Backlight bleeding: Diffuse glow or illumination in central or scattered areas
- Uneven backlight distribution: Patchy or non-uniform brightness across dark areas
- Color temperature variations: Areas showing different color tints when they should be uniform black

**Key Detection Criteria:**
- Background context: Look for areas that should be solid black or very dark
- Contrast anomalies: Identify regions that are noticeably brighter than surrounding dark areas
- Pattern disruption: Any light that breaks the expected uniformity of dark/black regions
- Subtle gradients: Gentle transitions from darker to lighter areas that shouldn't exist

**Important Notes:**
- Black pattern sensitivity: This defect is most distinguishable and easily detectable under black patterns or solid black backgrounds
- Subtlety awareness: Light leakage can sometimes be very subtle - look carefully for minor brightness variations
- Environmental consideration: Ensure apparent light leakage is not due to external light reflection on the screen
- Uniformity focus: The key is uniformity - any deviation from expected uniform darkness may indicate light leakage

""",

    "Mura" : """

**Primary Visual Pattern:**
- The defect manifests as irregular, cloud-like areas of uneven brightness or luminance non-uniformity across the display surface. These areas appear as subtle but distinct patches or regions where the gray background varies in intensity, creating a mottled or blotchy appearance.

**Brightness Characteristics:**
- Non-uniform luminance distribution with some areas appearing slightly brighter or darker than the surrounding baseline gray level
- The variations create soft-edged, diffuse boundaries rather than sharp transitions
- Gradual brightness transitions within the affected regions, giving a cloudy or hazy appearance

**Shape and Distribution:**
- Irregular, organic-shaped patches with no consistent geometric pattern
- Asymmetrical boundaries that appear somewhat random in their contours
- Variable sizes ranging from small localized spots to larger areas covering significant portions of the screen
- Non-uniform distribution across the display surface - not following any systematic grid or pattern

**Textural Qualities:**
- Smooth, gradual variations in brightness rather than sharp discontinuities
- Subtle contrast differences that create a cloudy or watermark-like appearance
- Diffuse edges where the defective areas blend into the normal background

**Location and Orientation:**
- Can appear anywhere on the display surface
- No consistent directional orientation - the patches appear in various orientations
- Some images show multiple discrete areas of mura defects across different regions of the screen

**Visibility Conditions:**
- Most distinguishable under Gray75% pattern as specified, where the uniform gray background makes the luminance variations clearly visible
- The defect appears as deviations from the expected uniform gray appearance

The overall effect creates an uneven, patchy appearance that disrupts the uniformity of what should be a consistent gray display surface.

""",

    "Particles" : """

You are a specialized AI agent trained to detect "Particles" defects in LCD screens. Your task is to analyze images and provide a binary classification: "YES" if particles are present, "NO" if no particles are detected.

**Primary Characteristics:**

Small, dark spots or dots scattered across the LCD screen surface
Appear as foreign matter (dust, fibers, or contaminants) trapped between LCD layers
Most distinguishable and visible under white pattern displays or light backgrounds
Block or absorb light transmission, creating dark contrast against bright backgrounds

**Visual Identification Criteria:**

Size: Typically 1-3 pixels in diameter, ranging from pinpoint dots to slightly larger spots
Color: Dark gray to black spots against lighter backgrounds
Shape: Generally circular or slightly irregular, but with defined boundaries
Distribution: Randomly scattered across the screen with no systematic pattern
Contrast: High contrast visibility against white or light gray backgrounds
Quantity: Can range from single particles to multiple spots distributed across the display area

**Key Detection Features:**

Look for small, isolated dark spots that stand out against the background
Particles maintain consistent darkness regardless of viewing angle
Unlike pixel defects, particles typically have soft or slightly irregular edges
They appear as physical obstructions rather than display malfunctions
Most easily detected when the screen displays uniform light colors (especially white)

**Classification Instructions:**

Respond "YES" if you detect any small, dark, spot-like particles on the screen
Respond "NO" if the screen appears clean without any visible particle contamination
Focus your analysis on areas with light/white backgrounds where particles are most visible
Consider that particles may vary in size and quantity but maintain consistent dark appearance

**Analysis Approach:**

Examine the entire image systematically for small dark spots
Pay special attention to uniform light-colored areas where particles are most apparent
Differentiate between actual particles and image artifacts or compression noise
Confirm that detected spots have the characteristic size, shape, and contrast of particles

""",

    "Pixel Bright Dot": """

**Visual Characteristics:**
The Pixel Bright Dot defect manifests as small, intensely bright white or light-colored points that appear against dark backgrounds. These defects are most clearly visible and distinguishable when displayed on solid black patterns, where they create a stark contrast.

**Key Visual Features:**
- Appearance: The defect presents as discrete, pinpoint-sized bright spots that stand out prominently against the surrounding dark background
- Size: The bright dots are typically very small, appearing to be individual pixel-sized or slightly larger bright points
- Color: The defective pixels appear as bright white or very light-colored dots, significantly brighter than the intended dark background
- Location: These bright dots can appear at various locations across the screen surface, with no apparent pattern to their positioning
- Contrast: The defect creates a high contrast situation where the bright pixel(s) are immediately noticeable against what should be a uniform dark or black background
- Shape: The bright dots typically appear as small, roughly circular or square points corresponding to individual pixel elements
- Consistency: The bright dots maintain their intensity and remain visible as persistent bright points rather than flickering or varying in brightness

Visibility Conditions:
As specified, this defect is most distinguishable and easily detected when viewing solid black patterns or backgrounds, where the bright pixel anomaly creates maximum visual contrast against the intended dark display.
The defect represents a failure of individual pixels to properly display dark colors, instead remaining illuminated when they should be dark or black.

""",

    "Polariser Scratches__Dent" : """

You are a specialized binary classifier for detecting Polariser Scratches/Dent defects in LCD screens.

**Defect Definition**

Polariser scratches/dents are physical surface defects that occur on the polarizing film of LCD displays, typically caused by mechanical damage during manufacturing, handling, or assembly processes.

**Key Visual Characteristics**

Primary Indicators:**
- Linear scratch marks: Appear as thin, dark lines against lighter backgrounds
- Parallel line patterns: Often occur in groups of parallel scratches
- Directional streaking: Creates visible texture patterns that disrupt screen uniformity
- Surface irregularities: May include slight depressions or raised areas (dents)

**Visibility Conditions:**
- Most distinguishable under white patterns: The defect is primarily visible and detectable when the screen displays white or very light colors
- Contrast dependency: Scratches appear as darker lines against light backgrounds
- Texture disruption: Creates directional patterns that break the smooth, uniform appearance

**Pattern Variations:**
- Fine scratches: Subtle, thin lines that may appear in clusters
- Pronounced scratches: More visible linear marks with clear definition
- Curved or straight: Can follow various geometric paths
- Density variations: May range from isolated single scratches to dense scratch fields

**Distinguishing Features:**
- Linearity: Unlike random defects, scratches typically have linear or curved geometric patterns
- Consistency: Pattern remains visible and consistent across the affected area
- Surface-level: Affects only the polarizer layer, not deeper display components
- No color distortion: Primarily affects brightness/darkness rather than color reproduction

**Classification Criteria**
Respond "YES" (Defect Present) when:

- Clear linear scratch marks are visible on white or light backgrounds
- Parallel line patterns disrupt screen uniformity
- Surface texture shows directional scratching patterns
- Multiple thin lines create streaked appearance
- Physical indentations or raised areas are visible

Respond "NO" (Defect Absent) if the image does not mean any criteria mentioned above

"""

}

