
import FreeCAD as App
import Part
import Draft
from FreeCAD import Base

# --- Parameters ---
STAMP_DIAMETER = 90.0
STAMP_HEIGHT = 15.0
TEXT_EXTRUSION_HEIGHT = 2.0
FONT_SIZE = 10  # Initial font size, will be scaled to fit
LINE_SPACING_FACTOR = 1.2 # Multiplier for font size to get line spacing
MARGIN = 0.95 # Use 95% of the diameter for the text width

# --- Text Content ---
# Note: The text is automatically mirrored.
TEXT_LINES = [
    "Merry Christmas",
    "love from",
    "Sara, Andrew,",
    "Dyaln and Kyle"
]

# --- Font Path ---
# Please adjust this path to a font file on your system if needed.
# Common Linux path: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
# Common Windows path: C:/Windows/Fonts/Arial.ttf
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def create_stamp():
    """
    Generates a 3D model of a circular stamp with specified text.
    """
    # --- Document Setup ---
    doc = App.newDocument("ChristmasStamp")

    # --- Create Base Cylinder ---
    radius = STAMP_DIAMETER / 2.0
    base_cylinder = Part.makeCylinder(radius, STAMP_HEIGHT)
    base_obj = doc.addObject("Part::Feature", "StampBase")
    base_obj.Shape = base_cylinder

    # --- Create and Combine Text Shapes (Centered) ---
    text_shape_objects = []
    line_height = FONT_SIZE * LINE_SPACING_FACTOR
    total_text_height = (len(TEXT_LINES) - 1) * line_height
    start_y = total_text_height / 2.0

    for i, line in enumerate(TEXT_LINES):
        shape_obj = Draft.make_shapestring(line, FONT_PATH, FONT_SIZE)
        
        # --- Center each line horizontally before stacking ---
        line_bounds = shape_obj.Shape.BoundBox
        center_x_offset = -(line_bounds.XMin + line_bounds.XMax) / 2.0
        
        # Create a vector to position the centered line
        position_vec = App.Vector(center_x_offset, start_y - (i * line_height), 0)
        
        # Move the shape's geometry directly
        Draft.move(shape_obj, position_vec)
        text_shape_objects.append(shape_obj)
    doc.recompute()

    # --- Fuse into a single shape for transformation ---
    if not text_shape_objects:
        print("No text shapes created. Aborting.")
        return

    fused_shape = text_shape_objects[0].Shape
    if len(text_shape_objects) > 1:
        fused_shape = fused_shape.fuse([s.Shape for s in text_shape_objects[1:]])

    # --- Calculate Transformations using Matrices ---
    bounds = fused_shape.BoundBox

    # 1. Vector to center the now-centered block (will mostly be Y-adjustment)
    center_vec = App.Vector(-(bounds.XMin + bounds.XMax) / 2.0, -(bounds.YMin + bounds.YMax) / 2.0, -bounds.ZMin)

    # 2. Scaling factor to fit the diameter
    text_width = bounds.XMax - bounds.XMin
    scale_factor = 1.0
    if text_width > (STAMP_DIAMETER * MARGIN):
        scale_factor = (STAMP_DIAMETER * MARGIN) / text_width

    # 3. Z position with a slight overlap for a good fuse
    Z_POSITION = STAMP_HEIGHT - 0.1

    # --- Build Combined Transformation Matrix ---
    center_matrix = App.Matrix()
    center_matrix.move(center_vec)

    scale_matrix = App.Matrix()
    scale_matrix.scale(scale_factor, scale_factor, 1.0) # Uniform XY scaling

    translate_matrix = App.Matrix()
    translate_matrix.move(App.Vector(0, 0, Z_POSITION))

    # Order of operations: Center -> Scale -> Translate
    final_matrix = translate_matrix.multiply(scale_matrix.multiply(center_matrix))

    # --- Apply Transformation ---
    transformed_shape = fused_shape.copy()
    transformed_shape.transformShape(final_matrix)

    # Create a new, clean object with the final transformed shape
    text_feature = doc.addObject("Part::Feature", "ProcessedText")
    text_feature.Shape = transformed_shape

    # Hide the original temporary shapes
    for obj in text_shape_objects:
        obj.ViewObject.Visibility = False
    doc.recompute()

    # --- Extrude Text ---
    extruded_text = doc.addObject("Part::Extrusion", "ExtrudedText")
    extruded_text.Base = text_feature
    extruded_text.Dir = App.Vector(0, 0, TEXT_EXTRUSION_HEIGHT)
    extruded_text.Solid = True
    doc.recompute()

    # --- Mirror the Extruded Text for Stamping ---
    mirrored_text = doc.addObject("Part::Mirroring", "MirroredText")
    mirrored_text.Source = extruded_text
    mirrored_text.Normal = App.Vector(1, 0, 0)  # YZ plane for horizontal flip
    mirrored_text.Base = text_feature.Shape.BoundBox.Center
    doc.recompute()

    # --- Fuse Base and Text ---
    stamp_final = doc.addObject("Part::Fuse", "Christmas_Stamp")
    stamp_final.Base = base_obj
    stamp_final.Tool = mirrored_text
    doc.recompute()

    # --- Clean Up Visibility ---
    for obj in [base_obj, text_feature, extruded_text, mirrored_text]:
        obj.ViewObject.Visibility = False
    stamp_final.ViewObject.Visibility = True
    doc.recompute()

    print("Stamp generation complete.")
    App.Gui.activeDocument().activeView().viewAxonometric()
    App.Gui.SendMsgToActiveView("ViewFit")

# --- Run the function ---
if App.Gui:
    create_stamp()
else:
    print("This script must be run from the FreeCAD GUI.")

