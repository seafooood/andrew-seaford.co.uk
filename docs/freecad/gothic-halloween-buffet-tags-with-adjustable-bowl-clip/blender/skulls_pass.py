"""Skulls theme for the buffet tag: two skulls peeking over the top corners, a skull
crest on the keystone, crossed bones on the bottom corners.

    blender -b --python blender/skulls_pass.py -- stl/buffet_tag_partA_blank.stl stl/buffet_tag_partA_skulls.stl
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tag_lib as T  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
src = argv[0] if argv else "stl/buffet_tag_partA_blank.stl"
dst = argv[1] if len(argv) > 1 else "stl/buffet_tag_partA_skulls.stl"


def rounded_rect(cx, cy, w, h, r, n=6):
    """Counter-clockwise rounded rectangle outline."""
    pts = []
    corners = [(cx + w / 2 - r, cy - h / 2 + r, -math.pi / 2), (cx + w / 2 - r, cy + h / 2 - r, 0.0),
               (cx - w / 2 + r, cy + h / 2 - r, math.pi / 2), (cx - w / 2 + r, cy - h / 2 + r, math.pi)]
    for x, y, a0 in corners:
        for i in range(n + 1):
            a = a0 + (math.pi / 2) * i / n
            pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    return pts


def skull(z, s=1.0, dome_h=2.4, jaw_h=1.8):
    """Skull built at the origin, facing +y up. s scales the footprint (s=1 ≈ 12 x 13 mm).
    Returns the finished skull object (dome cranium + jaw, with sockets, nose and teeth cut)."""
    cran = T.dome((0.0, 1.5 * s), 6.0 * s, 5.5 * s, dome_h, z, name="cranium")
    jaw = T.relief_from_outline(rounded_rect(0.0, -3.2 * s, 8.6 * s, 4.8 * s, 1.4 * s), z, jaw_h,
                                bevel=0.5 * s, name="jaw")
    T.union(cran, jaw)
    top = z + dome_h
    for ex in (-2.4, 2.4):                                              # eye sockets
        T.difference(cran, T.cutter_cylinder((ex * s, 2.3 * s), 1.65 * s, top, 1.5 * s + 0.2))
    T.difference(cran, T.cutter_cylinder((0.0, -0.1 * s), 0.95 * s, top, 1.0 * s + 0.2, vertices=3))  # nose
    for tx in (-2.4, -0.8, 0.8, 2.4):                                   # tooth grooves
        T.difference(cran, T.cutter_box((tx * s, -4.0 * s), 0.55 * s, 2.6 * s, z + jaw_h, 0.7 * s))
    T.difference(cran, T.cutter_box((0.0, -2.7 * s), 7.0 * s, 0.55 * s, z + jaw_h, 0.7 * s))  # gum line
    return cran


def crossed_bones(center, z, length=12.0, rot=0.0):
    objs = []
    for a in (math.pi / 4, -math.pi / 4):
        a += rot
        d = (math.cos(a), math.sin(a))
        p0 = (center[0] - d[0] * length / 2, center[1] - d[1] * length / 2)
        p1 = (center[0] + d[0] * length / 2, center[1] + d[1] * length / 2)
        objs.append(T.tube([p0, p1], 1.1, z, 1.4, name="bone"))
        side = (-d[1], d[0])
        for p in (p0, p1):                                              # knuckle knobs
            for sgn in (-1, 1):
                objs.append(T.dome((p[0] + side[0] * sgn * 1.05, p[1] + side[1] * sgn * 1.05), 1.45, 1.45, 1.7, z, name="knob"))
    return objs


# ---------------------------------------------------------------- build
T.setup_scene_mm()
frame = T.import_blank(src)
Z = T.FRONT_Z
parts = []

# big skulls peeking over the top corners
for sx in (-1, 1):
    ox, oy, rot, sc = sx * 36.5, 30.5, sx * math.radians(-10), 1.25
    foot = T.footprint_from_outline(T.ellipse((0.0, 1.5 * sc), 6.2 * sc, 5.7 * sc, n=40), "skull_foot")
    parts.append(T.place(foot, ox, oy, rot))
    parts.append(T.place(skull(Z, sc, dome_h=2.8, jaw_h=2.0), ox, oy, rot))

# skull crest on the keystone face
parts.append(T.place(skull(T.KEYSTONE_Z, 0.62, dome_h=1.6, jaw_h=1.2), 0.0, 34.4, 0.0))

# crossed bones on the bottom corners
for sx in (-1, 1):
    parts += crossed_bones((sx * 38.0, -28.3), Z, length=13.5, rot=sx * math.radians(8))

for ob in parts:
    T.union(frame, ob)

lo, hi = T.bounds(frame)
print(f"bounds x {lo.x:.1f}..{hi.x:.1f}  y {lo.y:.1f}..{hi.y:.1f}  z {lo.z:.2f}..{hi.z:.2f}")
print("non-manifold edges:", T.non_manifold_edges(frame))
assert lo.z > -0.01
T.export_stl(frame, dst)
print("exported", dst)
