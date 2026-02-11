import FreeCAD as App
import FreeCADGui as Gui
import Part
import Draft

# Create a new document, clearing any old ones
if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)
App.newDocument("SpoonKeyring")

# --- Spoon Dimensions ---
handle_length = 150.0   # The length of the straight handle part
handle_width = 22.0
spoon_thickness = 8.0   # A good thickness for a solid feel and concave cut

bowl_major_radius = 45.0 # How long the bowl is
bowl_minor_radius = 28.0 # How wide the bowl is

hole_diameter = 8.0

text_size = 12.0
text_depth = 1.5      # How deep the text is cut into the handle

# --- Build the 2D Profile ---

# 1. Create the rectangular part of the handle
p1 = App.Vector(handle_width / 2, -handle_width / 2, 0)
p2 = App.Vector(handle_length, -handle_width / 2, 0)
p3 = App.Vector(handle_length, handle_width / 2, 0)
p4 = App.Vector(handle_width / 2, handle_width / 2, 0)
handle_poly = Part.makePolygon([p1, p2, p3, p4, p1])
handle_face = Part.Face(handle_poly)

# 2. Create a circular cap for the end of the handle
end_cap_edge = Part.makeCircle(handle_width / 2, App.Vector(handle_width / 2, 0, 0), App.Vector(0, 0, 1))
end_cap_wire = Part.Wire([end_cap_edge])
end_cap_face = Part.Face(end_cap_wire)

# 3. Create the wider, elliptical bowl profile
overlap = 1.0 # Create a small overlap to ensure a clean boolean fusion
ellipse_center_x = handle_length - overlap
geom_ellipse = Part.Ellipse(App.Vector(ellipse_center_x, 0, 0), bowl_major_radius, bowl_minor_radius)
bowl_edge = geom_ellipse.toShape()
bowl_wire = Part.Wire([bowl_edge])
bowl_face = Part.Face(bowl_wire)

# 4. Fuse the three 2D faces into a single complete profile
base_profile = handle_face.fuse(end_cap_face)
spoon_profile = base_profile.fuse(bowl_face)

# 5. Create the keyring hole, centered in the rounded end
key_hole_edge = Part.makeCircle(hole_diameter / 2, App.Vector(handle_width / 2, 0, 0), App.Vector(0, 0, 1))
key_hole_wire = Part.Wire([key_hole_edge])
key_hole_face = Part.Face(key_hole_wire)

# 6. Cut the hole from the main 2D profile
final_profile = spoon_profile.cut(key_hole_face)

# --- Extrude Profile and Create 3D Features ---

# 7. Extrude the final 2D profile into the main 3D body
spoon_body = final_profile.extrude(App.Vector(0, 0, spoon_thickness))

# 8. Create a 3D cutting tool to make the BOWL CONCAVE on the BOTTOM surface
concave_radius = 150.0  # Using your preferred gentle curve
concave_sphere = Part.makeSphere(concave_radius)
sphere_pos_z = -concave_radius + spoon_thickness - 0.5 # Position sphere below to cut up
concave_sphere.translate(App.Vector(ellipse_center_x, 0, sphere_pos_z))
spoon_with_concave = spoon_body.cut(concave_sphere)

# 9. Create, MIRROR, and position the text cutter on the BOTTOM handle
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" # ADJUST IF NECESSARY
text_shape_object = Draft.make_shapestring(String="TOILET", FontFile=font_path, Size=text_size)

# CORRECTED: Mirror the 2D text shape horizontally to counteract the "bottom view" effect
original_2d_shape = text_shape_object.Shape
mirrored_2d_shape = original_2d_shape.mirror(App.Vector(0,0,0), App.Vector(0,1,0))

# Now, extrude the correctly oriented text UPWARDS to cut into the bottom face
text_solid = mirrored_2d_shape.extrude(App.Vector(0, 0, text_depth))

# Position the correctly oriented text solid using your code
text_bounds = text_solid.BoundBox
text_center_x = (handle_width/2) + (handle_length - handle_width/2)
text_pos_x = text_center_x - (text_bounds.XLength) - 60
text_pos_y = text_bounds.YLength / 2

# Place the text cutter's base at Z=0
text_solid.translate(App.Vector(text_pos_x, text_pos_y, 0))

final_spoon = spoon_with_concave.cut(text_solid)

# --- Finalize and Display ---
Part.show(final_spoon, "Spoon_Keyring")
App.ActiveDocument.removeObject(text_shape_object.Label) # Clean up

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")