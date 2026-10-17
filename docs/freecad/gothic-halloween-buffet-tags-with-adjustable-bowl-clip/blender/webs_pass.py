"""Spider-web theme for the buffet tag: quarter webs in all four corners, a spider on
the keystone, and a larger spider hanging from a thread into the top border.

    blender -b --python blender/webs_pass.py -- stl/buffet_tag_partA_blank.stl stl/buffet_tag_partA_webs.stl
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tag_lib as T  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
src = argv[0] if argv else "stl/buffet_tag_partA_blank.stl"
dst = argv[1] if len(argv) > 1 else "stl/buffet_tag_partA_webs.stl"

THREAD_R = 0.7        # web thread half-width (1.4 mm wide)
THREAD_H = 1.1        # web thread height above the face
LEG_R = 0.55
LEG_H = 0.8


def polar(c, r, a):
    return (c[0] + r * math.cos(a), c[1] + r * math.sin(a))


def web(hub, a0, a1, radius, z, radials=6, strands=(4.0, 7.5, 11.0, 14.0), sag=0.13):
    """Quarter web: radial threads fanning from hub between angles a0..a1, and sagging
    strands between neighbouring radials at each radius. Returns a list of tube objects."""
    objs = []
    angles = [a0 + (a1 - a0) * i / (radials - 1) for i in range(radials)]
    for a in angles:
        objs.append(T.tube([hub, polar(hub, radius, a)], THREAD_R, z, THREAD_H, name="radial"))
    for r in strands:
        if r > radius:
            continue
        for a, b in zip(angles, angles[1:]):
            pts = []
            for k in range(7):
                t = k / 6
                ang = a + (b - a) * t
                rr = r * (1 - sag * math.sin(math.pi * t))       # sags toward the hub mid-span
                pts.append(polar(hub, rr, ang))
            objs.append(T.tube(pts, THREAD_R, z, THREAD_H, name="strand"))
    return objs


def spider(center, size, z, up=(0.0, 1.0), leg_r=LEG_R, leg_h=LEG_H):
    """Spider with abdomen toward `up`, head opposite, four legs each side.
    `size` ≈ abdomen radius; overall span ≈ 5.5 * size."""
    ux, uy = up
    sx, sy = uy, -ux                       # 'right' vector
    def P(f, s_):                          # local (forward, side) -> world
        return (center[0] + ux * f + sx * s_, center[1] + uy * f + sy * s_)
    objs = []
    abd_c = P(0.9 * size, 0)
    head_c = P(-1.35 * size, 0)
    objs.append(T.dome(abd_c, size, size * 1.15, size * 0.85, z, name="abdomen"))
    objs.append(T.dome(head_c, size * 0.62, size * 0.62, size * 0.55, z, name="head"))
    # legs: (hip forward, knee forward, knee side, foot forward, foot side) in units of size
    legs = [(0.35, 1.25, 1.6, 1.9, 2.6),
            (0.10, 0.55, 1.9, 0.6, 2.9),
            (-0.20, -0.45, 1.85, -0.9, 2.8),
            (-0.55, -1.35, 1.5, -2.1, 2.3)]
    for hf, kf, ks, ff, fs in legs:
        for side in (-1, 1):
            path = [P(hf * size, side * 0.45 * size), P(kf * size, side * ks * size), P(ff * size, side * fs * size)]
            objs.append(T.tube(path, leg_r, z, leg_h, name="leg"))
    return objs


# ---------------------------------------------------------------- build
T.setup_scene_mm()
frame = T.import_blank(src)
Z = T.FRONT_Z
parts = []

# corner webs: hub just inside each corner bulge, fanning inward
for sx in (-1, 1):
    for sy in (-1, 1):
        hub = (sx * 41.0, sy * 31.0)
        # fan from "pointing along the top/bottom edge" to "pointing down/up the side"
        a_edge = math.atan2(0, -sx)                     # toward x = 0
        a_side = math.atan2(-sy, 0)                     # toward y = 0
        a0, a1 = sorted((a_edge, a_side))
        if a1 - a0 > math.pi:                           # take the short way round
            a0, a1 = a1, a0 + 2 * math.pi
        # top-right web is smaller to leave room for the hanging spider beside it
        parts += web(hub, a0, a1, 11.5 if (sx, sy) == (1, 1) else 14.0, Z)

# spider on the keystone face, head down toward the label
parts += spider((0.0, 35.4), 2.1, T.KEYSTONE_Z, up=(0.0, 1.0), leg_r=0.5, leg_h=0.7)

# hanging spider in the top border: thread from the top edge down to the abdomen
hx = 24.5
parts.append(T.tube([(hx, 31.8), (hx, 27.0)], 0.55, Z, 0.8, name="thread"))
parts += spider((hx, 24.8), 2.3, Z, up=(0.0, 1.0))

for ob in parts:
    T.union(frame, ob)

lo, hi = T.bounds(frame)
print(f"bounds x {lo.x:.1f}..{hi.x:.1f}  y {lo.y:.1f}..{hi.y:.1f}  z {lo.z:.2f}..{hi.z:.2f}")
print("non-manifold edges:", T.non_manifold_edges(frame))
assert lo.z > -0.01
T.export_stl(frame, dst)
print("exported", dst)
