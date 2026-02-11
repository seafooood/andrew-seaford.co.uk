import FreeCAD as App
import FreeCADGui as Gui
import Part
from FreeCAD import Base
import math

# Create a new document, clearing any old ones
if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)
App.newDocument("PrinterSafeStatorDisk")

# --- USER PARAMETERS (ADJUSTED FOR PRINTER) ---
# Maximum printable diameter is 240mm. We use 236mm (Radius 118mm) for safety.
MAX_DIAMETER_MM = 180.0
DISK_RADIUS = MAX_DIAMETER_MM / 2.0      # Outer radius of the final stator disk (118.0 mm)
DISK_THICKNESS = 4.0                    # Thickness of the stator disk (mm)

# Pocket Specifications
POCKET_COUNT = 27
POCKET_DIAMETER = 10.0
POCKET_DEPTH = 2.0

# Scaled PCD Radius: Reduced from 120.0 to fit within the new 118.0 radius.
PCD_RADIUS = 70.0                       # Pitch Circle Diameter (PCD) radius (100.0 mm)

# Central Hole Specifications
SHAFT_RADIUS = 22.0                      # Central hole radius for bearing (mm)

# --- MACRO START ---

# 1. Create the main solid disk and cut the shaft hole
disk_cylinder = Part.makeCylinder(DISK_RADIUS, DISK_THICKNESS)
shaft_cutter = Part.makeCylinder(SHAFT_RADIUS, DISK_THICKNESS)
stator_disk_base = disk_cylinder.cut(shaft_cutter)

# 2. Create the single circular pocket cutter
pocket_radius = POCKET_DIAMETER / 2.0
pocket_cutter = Part.makeCylinder(pocket_radius, POCKET_DEPTH)

# 3. Define the placement of the FIRST cutter (translated along X, offset in Z)
cutter_z_offset = DISK_THICKNESS - POCKET_DEPTH
initial_placement = App.Placement(App.Vector(PCD_RADIUS, 0, cutter_z_offset), App.Rotation(0, 0, 0))
pocket_cutter.Placement = initial_placement

# 4. Create the Polar Pattern of cutters (27 of them)
pocket_list = [] 
angle_step = 360.0 / POCKET_COUNT

for i in range(POCKET_COUNT):
    # Create a fresh copy of the original (translated) cutter
    next_cutter = pocket_cutter.copy()
    
    # Calculate the rotation angle
    angle = i * angle_step
    
    # Apply the rotation around the Z-axis (0,0,0)
    next_cutter.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), angle)
    
    # Add the cutter to the list
    pocket_list.append(next_cutter)

# Fuse all cutters together
all_pocket_cutters = Part.makeCompound(pocket_list)

# 7. Perform the final cut
final_stator = stator_disk_base.cut(all_pocket_cutters)

# --- Finalize and Display ---
Part.show(final_stator, "PrinterSafeStatorBody")

# Clean up temporary Part objects
for obj in App.ActiveDocument.Objects:
    if obj.Name != 'PrinterSafeStatorBody' and hasattr(obj, 'Shape'):
        App.ActiveDocument.removeObject(obj.Name)

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")