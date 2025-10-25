import FreeCAD as App
import FreeCADGui as Gui
import Part
from FreeCAD import Base
import math

# Create a new document, clearing any old ones
if App.ActiveDocument:
    App.closeDocument(App.ActiveDocument.Name)
App.newDocument("RotorDisk")

# --- USER PARAMETERS ---
# Overall Disk Dimensions (Adjust these if necessary)
DISK_RADIUS = 90.0      
DISK_THICKNESS = 4.0    

# Magnet Pocket Specifications
MAGNET_COUNT = 36
MAGNET_WIDTH = 7.1 + 0.1  # Width of the pocket (along the radius)
MAGNET_LENGTH = 2.7 + 0.1 # Length of the pocket (circumferential)
POCKET_DEPTH = 2.0 + 0.1  # Depth of the pocket
PCD_RADIUS = 70.0        # Pitch Circle Diameter (PCD) radius for magnet centers
SKEW_ANGLE = 7.5          # Skew angle in degrees

# Center Shaft Hole Specifications
SHAFT_RADIUS = 22.0       # Radius of the central hole (mm)

# --- MACRO START ---

# 1. Create the main solid disk and cut the shaft hole
disk_cylinder = Part.makeCylinder(DISK_RADIUS, DISK_THICKNESS)
shaft_cutter = Part.makeCylinder(SHAFT_RADIUS, DISK_THICKNESS)
rotor_disk_base = disk_cylinder.cut(shaft_cutter)

# 2. Define the single magnet pocket cutter (rectangular box)
# The pocket depth cut starts from the top surface (Z = DISK_THICKNESS - POCKET_DEPTH)
pocket_box = Part.makeBox(MAGNET_WIDTH, MAGNET_LENGTH, POCKET_DEPTH)

# 3. Define the base placement (translation) for the first pocket
# The box origin is (0,0,0). To center the pocket on the PCD, we need to translate it.
# X-position: The center of the pocket should be at PCD_RADIUS.
initial_x_translation = PCD_RADIUS - (MAGNET_WIDTH / 2.0)
initial_y_translation = - (MAGNET_LENGTH / 2.0)
initial_z_translation = DISK_THICKNESS - POCKET_DEPTH # Place the cut correctly on the top surface

base_placement = App.Placement(
    App.Vector(initial_x_translation, initial_y_translation, initial_z_translation), 
    App.Rotation(App.Vector(0, 0, 1), 0.0) # Start with 0 rotation
)

# 4. Create the final cutting tool by fusing all 36 skewed and rotated pockets
all_magnet_cutters = Part.Shape() # Initialize an empty shape to build the cutter compound
angle_step = 360.0 / MAGNET_COUNT

for i in range(MAGNET_COUNT):
    # Calculate the total angle for this pocket (position angle + skew)
    position_angle = i * angle_step
    total_rotation_angle = position_angle + SKEW_ANGLE

    # 4a. Create a fresh copy of the pocket box
    current_cutter = pocket_box.copy()
    
    # 4b. Apply the base placement (translation)
    current_cutter.Placement = base_placement
    
    # 4c. Apply the combined rotation around the Z-axis (at the origin 0,0,0)
    # This correctly rotates the entire translated pocket around the center of the disk.
    current_cutter.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), total_rotation_angle)
    
    # 4d. Fuse or Compound the new cutter to the overall cutting tool
    if i == 0:
        all_magnet_cutters = current_cutter
    else:
        # Use fuse() for robust Boolean operations in Part Workbench
        all_magnet_cutters = all_magnet_cutters.fuse(current_cutter)


# 5. Perform the final cut
final_rotor = rotor_disk_base.cut(all_magnet_cutters)

# --- Finalize and Display ---
Part.show(final_rotor, "RotorDiskBody")

# Clean up temporary Part objects from the document tree (only objects added by Part.show)
for obj in App.ActiveDocument.Objects:
    if obj.Name != 'RotorDiskBody' and hasattr(obj, 'Shape'):
        App.ActiveDocument.removeObject(obj.Name)

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")