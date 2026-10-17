"""Ghosts theme for the buffet tag: two ghosts peeking over the top corners with their
hands on the moulding, a small ghost on the keystone, two little ghosts drifting up from
the bottom corners.

    blender -b --python blender/ghosts_pass.py -- stl/buffet_tag_partA_blank.stl stl/buffet_tag_partA_ghosts.stl
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tag_lib as T  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
src = argv[0] if argv else "stl/buffet_tag_partA_blank.stl"
dst = argv[1] if len(argv) > 1 else "stl/buffet_tag_partA_ghosts.stl"


# ---------------------------------------------------------------- outlines (local coords, y up)
def scallops(x0, x1, y, n, amp, steps=6, down=True):
    """Points along a wavy edge from x0 to x1 at height y, n scallops dipping by amp."""
    pts = []
    for i in range(n):
        for k in range(steps):
            t = (i + k / steps) / n
            u = (k / steps)
            dip = amp * math.sin(math.pi * u)
            pts.append((x0 + (x1 - x0) * t, y - dip if down else y + dip))
    return pts


def peeking_ghost(w=16.0, h=13.0, hem_y=0.0):
    """Head and shoulders only: flat bottom at hem_y (hidden behind the frame edge),
    round head on top. Origin at bottom centre. Counter-clockwise."""
    r = w / 2
    cy = hem_y + h - r
    pts = [(r, hem_y)]
    # head arc from angle 0 (right) over the top to 180 (left)
    for i in range(0, 25):
        a = math.pi * i / 24
        pts.append((r * math.cos(a), cy + r * math.sin(a)))
    pts.append((-r, hem_y))
    return pts


def hand(w=5.0, h=5.0, fingers=3):
    """A blob with a straight top (merges into the ghost) and finger bumps below.
    Origin at top centre. Counter-clockwise."""
    pts = [(w / 2, 0.0), (w / 2, -h + 1.5)]
    pts += scallops(w / 2, -w / 2, -h + 1.5, fingers, 1.5, steps=6, down=True)
    pts += [(-w / 2, -h + 1.5), (-w / 2, 0.0)]
    return pts


def little_ghost(w=9.0, h=12.0):
    """Classic ghost: round head, wavy hem. Origin at hem centre. Counter-clockwise."""
    r = w / 2
    cy = h - r
    pts = [(r * 1.08, 0.0), (r * 1.02, cy * 0.5)]
    for i in range(0, 25):
        a = math.pi * i / 24
        pts.append((r * math.cos(a), cy + r * math.sin(a)))
    pts += [(-r * 1.02, cy * 0.5), (-r * 1.08, 0.0)]
    pts += scallops(-r * 1.08, r * 1.08, 0.0, 4, 1.6, steps=5, down=True)
    return pts


# ---------------------------------------------------------------- build
T.setup_scene_mm()
frame = T.import_blank(src)
Z = T.FRONT_Z
parts = []      # (object, is_footprint)

# --- big peeking ghosts, top corners ---
for sx in (-1, 1):
    ox, oy, rot = sx * 36.0, 30.0, sx * math.radians(-8)
    body = T.transform_pts(peeking_ghost(16, 13), dx=ox, dy=oy, rot=rot)
    parts.append(T.footprint_from_outline(body, "ghost_foot"))
    g = T.relief_from_outline(body, Z, 2.6, bevel=1.0, name="ghost")
    # face: two eyes and an "oh" mouth, recessed 1.2 mm
    for ex in (-2.7, 2.7):
        T.difference(g, T.cutter_cylinder(T.transform_pts([(ex, 7.6)], dx=ox, dy=oy, rot=rot)[0], 1.45, Z + 2.6, 1.3))
    T.difference(g, T.cutter_cylinder(T.transform_pts([(0.0, 3.4)], dx=ox, dy=oy, rot=rot)[0], 1.25, Z + 2.6, 1.3))
    parts.append(g)
    # hands over the moulding, hanging from the flat bottom edge
    for hx in (-5.5, 5.5):
        hp = T.transform_pts(hand(4.6, 5.0), dx=ox, dy=oy + 0.6, rot=rot)
        hp = [(x + hx * math.cos(rot), y + hx * math.sin(rot)) for x, y in hp]
        parts.append(T.footprint_from_outline(hp, "hand_foot"))
        parts.append(T.relief_from_outline(hp, Z, 2.2, bevel=0.8, name="hand"))

# --- small ghost on the keystone face ---
kg = T.transform_pts(little_ghost(7.0, 8.6), dx=0.0, dy=30.9)
kob = T.relief_from_outline(kg, T.KEYSTONE_Z, 1.3, bevel=0.45, name="keystone_ghost")
for ex in (-1.3, 1.3):
    T.difference(kob, T.cutter_cylinder((ex, 36.4), 0.6, T.KEYSTONE_Z + 1.3, 0.6))
T.difference(kob, T.cutter_cylinder((0.0, 34.6), 0.5, T.KEYSTONE_Z + 1.3, 0.6))
parts.append(kob)

# --- little ghosts drifting up from the bottom corners ---
for sx in (-1, 1):
    ox, oy, rot = sx * 38.0, -33.0, sx * math.radians(14)
    lg = T.transform_pts(little_ghost(9.0, 12.0), dx=ox, dy=oy, rot=rot)
    parts.append(T.footprint_from_outline(lg, "lg_foot"))
    g = T.relief_from_outline(lg, Z, 2.2, bevel=0.8, name="little_ghost")
    for ex in (-1.6, 1.6):
        T.difference(g, T.cutter_cylinder(T.transform_pts([(ex, 8.2)], dx=ox, dy=oy, rot=rot)[0], 0.75, Z + 2.2, 0.9))
    T.difference(g, T.cutter_cylinder(T.transform_pts([(0.0, 5.6)], dx=ox, dy=oy, rot=rot)[0], 0.65, Z + 2.2, 0.9))
    parts.append(g)

for ob in parts:
    T.union(frame, ob)

lo, hi = T.bounds(frame)
print(f"bounds x {lo.x:.1f}..{hi.x:.1f}  y {lo.y:.1f}..{hi.y:.1f}  z {lo.z:.2f}..{hi.z:.2f}")
print("non-manifold edges:", T.non_manifold_edges(frame))
assert lo.z > -0.01
T.export_stl(frame, dst)
print("exported", dst)
