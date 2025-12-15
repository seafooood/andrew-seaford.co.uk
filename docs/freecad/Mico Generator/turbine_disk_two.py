import FreeCAD as App
import FreeCADGui as Gui
import Part
from FreeCAD import Base
import math

# Create a new document, clearing any old ones
if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)
App.newDocument("StatorDisk")

# --- USER PARAMETERS ---
# Overall Disk Dimensions
DISK_RADIUS = 90.0      # Outer radius of the final stator disk (mm)
DISK_THICKNESS = 4.0    # Thickness of the stator disk (mm)

# Coil/Tooth Specifications
TOOTH_COUNT = 27
SHAFT_RADIUS = 22.0      # Central hole radius for bearing (mm)

# Radial Dimensions of the Coil Posts (ADJUST THESE TO YOUR OPTIMIZED VALUES)
TOOTH_INNER_RADIUS = 60.0  # Di/2 (Inner radius of the coil posts)
TOOTH_OUTER_RADIUS = 80.0 # Do/2 (Outer radius of the coil posts)

# Angular Dimensions
SLOT_WIDTH_ANGLE = 5.0   # The actual angle of the empty slot gap
ANGLE_PER_SEGMENT = 360.0 / TOOTH_COUNT # Total angle for one tooth/slot segment (~13.33 degrees)

# Structural dimensions
STRUCTURAL_OUTER_RADIUS = DISK_RADIUS 
HUB_OUTER_RADIUS = TOOTH_INNER_RADIUS 
BACK_IRON_INNER_RADIUS = TOOTH_OUTER_RADIUS 
BACK_IRON_OUTER_RADIUS = DISK_RADIUS 
tooth_arc_angle = ANGLE_PER_SEGMENT - SLOT_WIDTH_ANGLE

# --- MACRO START ---

# 1. DEFINE THE SINGLE TOOTH POST GEOMETRY (Solid part)
half_tooth_angle = tooth_arc_angle / 2.0 
P1_angle = -half_tooth_angle
P4_angle = half_tooth_angle

P1_rad = math.radians(P1_angle)
P4_rad = math.radians(P4_angle)

P1 = App.Vector(TOOTH_INNER_RADIUS * math.cos(P1_rad), TOOTH_INNER_RADIUS * math.sin(P1_rad), 0)
P4 = App.Vector(TOOTH_INNER_RADIUS * math.cos(P4_rad), TOOTH_INNER_RADIUS * math.sin(P4_rad), 0)
P2 = App.Vector(TOOTH_OUTER_RADIUS * math.cos(P1_rad), TOOTH_OUTER_RADIUS * math.sin(P1_rad), 0)
P3 = App.Vector(TOOTH_OUTER_RADIUS * math.cos(P4_rad), TOOTH_OUTER_RADIUS * math.sin(P4_rad), 0)

line1 = Part.makeLine(P1, P2) 
line2 = Part.makeLine(P4, P3) 
arc_outer = Part.makeCircle(TOOTH_OUTER_RADIUS, App.Vector(0, 0, 0), App.Vector(0, 0, 1), P1_angle, P4_angle)
arc_inner = Part.makeCircle(TOOTH_INNER_RADIUS, App.Vector(0, 0, 0), App.Vector(0, 0, 1), P4_angle, P1_angle)
arc_inner.reverse() 

tooth_profile_wire = Part.Wire([line1, arc_outer, line2, arc_inner])
tooth_profile_face = Part.Face(tooth_profile_wire)
single_tooth_post = tooth_profile_face.extrude(App.Vector(0, 0, DISK_THICKNESS))


# 2. CREATE ALL 27 TEETH
tooth_list = []
for i in range(TOOTH_COUNT):
    next_tooth = single_tooth_post.copy()
    angle = i * ANGLE_PER_SEGMENT
    rotation_placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1), angle))
    next_tooth.Placement = rotation_placement
    tooth_list.append(next_tooth)

all_teeth = Part.makeCompound(tooth_list)


# 3. CREATE THE CENTRAL HUB (Inner Back Iron)
# Annular ring from SHAFT_RADIUS to HUB_OUTER_RADIUS
# NOTE: The center hole will be filled by fusing with teeth, so we create the solid Hub for now.
central_hub = Part.makeCylinder(HUB_OUTER_RADIUS, DISK_THICKNESS)


# 4. CREATE THE OUTER BACK IRON (Connecting the outer edges)
outer_ring = Part.makeCylinder(BACK_IRON_OUTER_RADIUS, DISK_THICKNESS)
outer_ring_cutter = Part.makeCylinder(BACK_IRON_INNER_RADIUS, DISK_THICKNESS)
outer_back_iron = outer_ring.cut(outer_ring_cutter)


# 5. FUSE ALL COMPONENTS TOGETHER
structural_base = central_hub.fuse(outer_back_iron)
stator_body = structural_base.fuse(all_teeth)

# 6. CUT THE FINAL SHAFT HOLE (FIXED STEP)
shaft_cutter = Part.makeCylinder(SHAFT_RADIUS, DISK_THICKNESS)
final_stator = stator_body.cut(shaft_cutter)

# 7. Center the entire stator geometry
final_stator.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), ANGLE_PER_SEGMENT / 2.0)

# --- Finalize and Display ---
Part.show(final_stator, "StatorDiskBody")

# Clean up temporary objects left in the document (only objects added by Part.show)
for obj in App.ActiveDocument.Objects:
    if obj.Name != 'StatorDiskBody' and hasattr(obj, 'Shape'):
        App.ActiveDocument.removeObject(obj.Name)

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")