import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft

# Create a new document, clearing any old ones
if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)
App.newDocument("SpannerKeyring")

# --- Spanner Dimensions ---
spanner_length = 180.0
spanner_width = 30.0
spanner_thickness = 8.0
head_diameter = 60.0
jaw_opening_width = 32.0
jaw_angle = 15.0      # Angle of the spanner jaw
hole_diameter = 8.0
hole_margin_from_end = 15.0 # Distance of hole center from the very end of the rounded part
text_size = 20.0
text_depth = 2.0

# --- Build the 2D Profile (without the jaw cut) ---

# 1. Create the rectangular part of the handle
handle_rect_length = spanner_length - (spanner_width / 2)
p1 = App.Vector(-handle_rect_length, -spanner_width / 2, 0)
p2 = App.Vector(0, -spanner_width / 2, 0)
p3 = App.Vector(0, spanner_width / 2, 0)
p4 = App.Vector(-handle_rect_length, spanner_width / 2, 0)
handle_poly = Part.makePolygon([p1, p2, p3, p4, p1])
handle_face = Part.Face(handle_poly)

# 2. Create a circular cap for the end of the handle
end_cap_edge = Part.makeCircle(spanner_width / 2, App.Vector(-handle_rect_length, 0, 0), App.Vector(0, 0, 1))
end_cap_wire = Part.Wire([end_cap_edge])
end_cap_face = Part.Face(end_cap_wire)

# 3. Create the full circular head
head_edge = Part.makeCircle(head_diameter / 2, App.Vector(0, 0, 0), App.Vector(0, 0, 1))
head_wire = Part.Wire([head_edge])
head_face = Part.Face(head_wire)

# 4. Fuse the three 2D faces into a single complete profile
base_profile = handle_face.fuse(end_cap_face)
spanner_profile = base_profile.fuse(head_face)

# 5. Create the 2D shape for the key hole
hole_center_x = -spanner_length + hole_margin_from_end
key_hole_edge = Part.makeCircle(hole_diameter / 2, App.Vector(hole_center_x, 0, 0), App.Vector(0, 0, 1))
key_hole_wire = Part.Wire([key_hole_edge])
key_hole_face = Part.Face(key_hole_wire)

# 6. Cut only the hole from the 2D profile
profile_with_hole = spanner_profile.cut(key_hole_face)

# --- Extrude the Profile and Perform 3D Cuts ---

# 7. Extrude the 2D profile into a 3D solid
spanner_body = profile_with_hole.extrude(App.Vector(0, 0, spanner_thickness))

# 8. CORRECTED: Create a 3D cutting tool for the jaw
jaw_cutter = Part.makeBox(head_diameter, jaw_opening_width, spanner_thickness)
jaw_cutter.translate(App.Vector(-10, -jaw_opening_width / 2, 0)) # Center the box
# Rotate and position the 3D cutter
jaw_cutter.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), jaw_angle)
jaw_cutter.translate(App.Vector(head_diameter / 4, 0, 0))

# 9. Perform the jaw cutout as a 3D boolean operation
spanner_body_with_jaw = spanner_body.cut(jaw_cutter)

# --- Create and Cut the "TOILET" Text ---
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" # ADJUST IF NECESSARY

text_shape = Draft.make_shapestring(String="TOILET", FontFile=font_path, Size=text_size)
# Extrude the text downwards to create a cutting tool
text_solid = text_shape.Shape.extrude(App.Vector(0, 0, -text_depth))

# Position the text cutting tool
text_bounds = text_shape.Shape.BoundBox
text_center_x = -handle_rect_length / 2 # Center text on the rectangular part
text_pos_x = text_center_x - (text_bounds.XLength / 2)
text_pos_y = -text_bounds.YLength / 2
placement = App.Placement(App.Vector(text_pos_x, text_pos_y, spanner_thickness), App.Rotation(App.Vector(0,0,0), 0))
text_solid.Placement = placement

final_keyring = spanner_body_with_jaw.cut(text_solid)

# --- Finalize and Display ---
Part.show(final_keyring, "Spanner_Keyring")
App.ActiveDocument.removeObject(text_shape.Label) # Clean up intermediate Draft object

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")