import FreeCAD as App
import Part
import Draft
import os

# --- CONFIGURATION ---
text_content = "SAM"
letter_size = 52.0 # The height of the letters
extrude_depth = 24.0 # The "thick" the letters are (front-to-back)
plate_thickness = 4.0 # Base plate thickness
h1_rad = 1.5 # --- Hole 1: 3mm width (1.5mm rad), 2mm from bottom ---
h2_rad = 4.5 # --- Hole 2: 7mm width (4.5mm rad), halfway from bottom ---
max_print_size = 200.0 # Max X dimension the printer can handle (mm)
char_width_ratio = 0.65 # Conservative estimate of char width relative to letter_size

# --- AUTO-ADJUST LETTER SIZE TO FIT PRINT AREA ---
estimated_width = letter_size * len(text_content) * char_width_ratio
if estimated_width > max_print_size:
    letter_size = max_print_size / (len(text_content) * char_width_ratio)
    App.Console.PrintMessage(f"Letter size adjusted to {letter_size:.1f}mm to fit within {max_print_size}mm print area.\n")


# Ubuntu font paths
possible_fonts = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
]

font_path = next((p for p in possible_fonts if os.path.exists(p)), None)

if not font_path:
    App.Console.PrintError("Error: No font file found.\n")
else:
    doc = App.newDocument("DARTS")

    # 1. Create ShapeString
    shapestring = Draft.makeShapeString(String=text_content, FontFile=font_path, Size=letter_size)
    
    # 2. ROTATE 90 DEGREES (Standing up)
    # Rotate around X-axis so it stands on the XY plane
    shapestring.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(1,0,0), 90))
    doc.recompute()

    # 3. EXTRUDE (thickness in Y direction)
    # Since we rotated, we extrude "backwards" or "forwards"
    letters_shape = shapestring.Shape.extrude(App.Vector(0, extrude_depth, 0))
    letters_obj = doc.addObject("Part::Feature", "Letters")
    letters_obj.Shape = letters_shape

    # 4. Create Base Plate based on the NEW footprint
    bbox = letters_shape.BoundBox
    # Width is X, Depth is Y
    plate_width = bbox.XMax - bbox.XMin
    plate_depth = bbox.YMax - bbox.YMin

    base_plate = Part.makeBox(plate_width, plate_depth, plate_thickness)
    # Position plate directly under the letters
    base_plate.translate(App.Vector(bbox.XMin, bbox.YMin, -plate_thickness))

    plate_obj = doc.addObject("Part::Feature", "BasePlate")
    plate_obj.Shape = base_plate

    # 4b. Create Top Plate above the letters
    top_plate_overlap = 2.0  # Overlap into letters to close gaps at letter peaks
    top_plate = Part.makeBox(plate_width, plate_depth, plate_thickness)
    # Position plate slightly overlapping the letter tops to eliminate gaps
    top_plate.translate(App.Vector(bbox.XMin, bbox.YMin, bbox.ZMax - top_plate_overlap))

    top_plate_obj = doc.addObject("Part::Feature", "TopPlate")
    top_plate_obj.Shape = top_plate

    # Fuse them
    combined_shape = letters_obj.Shape.fuse(plate_obj.Shape).fuse(top_plate_obj.Shape)

    # 5. HOLE CALCULATIONS
    # Total height = Top of top plate to Bottom of base plate
    bottom_z = -plate_thickness
    top_z = bbox.ZMax - top_plate_overlap + plate_thickness
    total_z_height = top_z - bottom_z

    num_holes = 3
    char_centers_x = []
    step = plate_width / num_holes
    for i in range(num_holes):
        char_centers_x.append(bbox.XMin + (step * i) + (step / 2))

    center_y = bbox.YMin + (plate_depth / 2)

    all_holes = []
    for cx in char_centers_x:
        # --- Hole 1: 3mm width (1.5mm rad), 2mm from bottom ---
        # Depth = total height - 2mm
        h1_depth = total_z_height - 2.0
        hole1 = Part.makeCylinder(h1_rad, h1_depth)
        hole1.translate(App.Vector(cx, center_y, top_z - h1_depth))
        all_holes.append(hole1)

        # --- Hole 2: 6mm width (4.0mm rad), halfway from bottom ---
        h2_depth = total_z_height / 2.0
        hole2 = Part.makeCylinder(h2_rad, h2_depth)
        hole2.translate(App.Vector(cx, center_y, top_z - h2_depth))
        all_holes.append(hole2)

    # 6. Final Cut
    final_shape = combined_shape
    for h in all_holes:
        final_shape = final_shape.cut(h)

    result_obj = doc.addObject("Part::Feature", "Final_Standing_Model")
    result_obj.Shape = final_shape

    # Cleanup
    doc.removeObject(letters_obj.Name)
    doc.removeObject(plate_obj.Name)
    doc.removeObject(top_plate_obj.Name)
    shapestring.ViewObject.hide()

    doc.recompute()
    App.Gui.ActiveDocument.ActiveView.viewAxometric()
    App.Gui.SendMsgToActiveView("ViewFit")