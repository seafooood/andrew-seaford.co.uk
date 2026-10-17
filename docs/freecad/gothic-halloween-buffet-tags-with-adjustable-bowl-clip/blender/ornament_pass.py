"""Minimal example of an ornament pass on the buffet-tag blank, using tag_lib.
Copy this file for a new theme; see ghosts_pass.py and webs_pass.py for real ones.

    blender -b --python blender/ornament_pass.py -- stl/buffet_tag_partA_blank.stl stl/buffet_tag_partA_example.stl
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tag_lib as T  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
src = argv[0] if argv else "stl/buffet_tag_partA_blank.stl"
dst = argv[1] if len(argv) > 1 else "stl/buffet_tag_partA_example.stl"

T.setup_scene_mm()
frame = T.import_blank(src)
parts = []

# a dome breaking the outline at each top corner: relief on the front face plus its own
# full-depth footprint so the overhanging part has plate under it
for sx in (-1, 1):
    outline = T.ellipse((sx * 36, 31), 6, 6)
    parts.append(T.footprint_from_outline(outline))
    parts.append(T.dome((sx * 36, 31), 6, 6, 2.2, T.FRONT_Z))

# a raised ring on the keystone face (stays inside the 20 x 10 face)
ring = T.ellipse((0, 35.3), 3.5, 3.5, n=48)
parts.append(T.relief_from_outline(ring, T.KEYSTONE_Z, 1.2, bevel=0.4))
T.difference(parts[-1], T.cutter_cylinder((0, 35.3), 2.2, T.KEYSTONE_Z + 1.2, 2.0))

for ob in parts:
    T.union(frame, ob)

lo, hi = T.bounds(frame)
print(f"bounds x {lo.x:.1f}..{hi.x:.1f}  y {lo.y:.1f}..{hi.y:.1f}  z {lo.z:.2f}..{hi.z:.2f}")
print("non-manifold edges:", T.non_manifold_edges(frame))
assert lo.z > -0.01, "geometry below the back face: would not sit flat on the bed"
T.export_stl(frame, dst)
print("exported", dst)
