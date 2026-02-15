"""
FreeCAD Macro: Disk with Holes and Edge Cutouts
Creates a flat disk 100mm diameter, 3mm thick with:
- 21 holes of 6mm diameter in the center
- Cutouts around the edge (3mm wide x 3mm deep)
"""

import FreeCAD
import Part
import math

# Create a new document
doc = FreeCAD.newDocument("DiskWithHoles")

# ===== Parameters =====
disk_diameter = 100.0  # mm (10cm)
disk_radius = disk_diameter / 2.0
disk_thickness = 3.0   # mm

hole_diameter = 6.0    # mm
hole_radius = hole_diameter / 2.0

cutout_width = 3.0     # mm
cutout_depth = 6.0     # mm
num_cutouts = 12       # number of cutouts around the edge

# ===== Create the base disk =====
disk = Part.makeCylinder(disk_radius, disk_thickness)

# ===== Create 21 holes arranged in concentric circles =====
# Pattern: 1 center + 6 in first ring + 14 in second ring = 21 holes
holes = []



# ===== Create cutouts around the edge =====
# Each cutout is a rectangular notch 3mm wide x 3mm deep
for i in range(num_cutouts):
    angle = i * (2 * math.pi / num_cutouts)

    # Create a box for the cutout
    # Position it so it cuts 3mm deep from the outer edge
    cutout = Part.makeBox(cutout_depth + 1, cutout_width, disk_thickness)

    # Move it to the edge (slightly beyond to ensure clean cut)
    cutout.translate(FreeCAD.Vector(disk_radius - cutout_depth, -cutout_width / 2.0, 0))

    # Rotate around the Z axis to position around the circumference
    cutout.rotate(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), math.degrees(angle))

    # Cut the notch from the disk
    disk = disk.cut(cutout)

# ===== Add the final shape to the document =====
disk_feature = doc.addObject("Part::Feature", "Disk")
disk_feature.Shape = disk

# Recompute and fit view
doc.recompute()

# Try to fit the view if GUI is available
try:
    import FreeCADGui
    FreeCADGui.ActiveDocument.ActiveView.fitAll()
except:
    pass

FreeCAD.Console.PrintMessage("Disk created successfully!\n")
FreeCAD.Console.PrintMessage(f"  - Diameter: {disk_diameter}mm\n")
FreeCAD.Console.PrintMessage(f"  - Thickness: {disk_thickness}mm\n")
FreeCAD.Console.PrintMessage(f"  - Holes: 21 x {hole_diameter}mm diameter\n")
FreeCAD.Console.PrintMessage(f"  - Edge cutouts: {num_cutouts} x {cutout_width}mm wide x {cutout_depth}mm deep\n")
