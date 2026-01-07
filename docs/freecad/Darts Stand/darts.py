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

    # Fuse them
    combined_shape = letters_obj.Shape.fuse(plate_obj.Shape)

    # 5. HOLE CALCULATIONS
    # Total height = Top of letter to Bottom of plate
    total_z_height = bbox.ZMax - (-plate_thickness) 
    top_z = bbox.ZMax
    bottom_z = -plate_thickness

    char_centers_x = []
    step = plate_width / len(text_content)
    for i in range(len(text_content)):
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
    shapestring.ViewObject.hide()

    doc.recompute()
    App.Gui.ActiveDocument.ActiveView.viewAxometric()
    App.Gui.SendMsgToActiveView("ViewFit")