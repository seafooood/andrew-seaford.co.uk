"""Shared helpers for ornament passes on the buffet-tag blank (Blender 4.x/5.x, headless).

Coordinates are the blank STL's, in mm, print orientation:
    back face z = 0 · front face z = 3.0 · moulding tops z = 4.5 · keystone face z = 12.5
    keystone x ∈ [-10, 10], y ∈ [30.3, 40.3] · label recess x ∈ [-32, 32], y ∈ [-19.3, 19.3] (keep clear)
    socket x ∈ [-6.2, 6.2], y ∈ [33.4, 37.2], z ∈ [0, 11] (keep clear)
"""
import math
import bpy
import bmesh
from mathutils import Vector

FRONT_Z = 3.0
KEYSTONE_Z = 12.5
PLATE_T = 3.0
EMBED = 0.15          # how far ornament bases sink into the surface so the boolean fuses


# ---------------------------------------------------------------- scene / io
def setup_scene_mm():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.unit_settings.system = "METRIC"
    s.unit_settings.length_unit = "MILLIMETERS"
    s.unit_settings.scale_length = 0.001


def import_blank(path):
    bpy.ops.wm.stl_import(filepath=path, global_scale=1.0)
    ob = bpy.context.selected_objects[0]
    ob.name = "PartA"
    return ob


def export_stl(ob, path):
    bpy.ops.object.select_all(action="DESELECT")
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.wm.stl_export(filepath=path, export_selected_objects=True, global_scale=1.0)


def bounds(ob):
    bb = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
    lo = Vector((min(v.x for v in bb), min(v.y for v in bb), min(v.z for v in bb)))
    hi = Vector((max(v.x for v in bb), max(v.y for v in bb), max(v.z for v in bb)))
    return lo, hi


def non_manifold_edges(ob):
    """Edges not shared by exactly two faces, after merging coincident vertices."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    n = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return n


# ---------------------------------------------------------------- mesh builders
def _obj_from_bmesh(bm, name):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    return ob


def relief_from_outline(pts, z0, height, bevel=0.0, bevel_segments=4, name="relief"):
    """Extrude a closed 2D outline (list of (x, y), counter-clockwise, no self-intersection)
    from z0 - EMBED up to z0 + height. Optional bevel rounds only the TOP edges, so the
    base stays vertical (a rounded base would be a downward overhang on the print)."""
    bm = bmesh.new()
    verts = [bm.verts.new((x, y, z0 - EMBED)) for x, y in pts]
    face = bm.faces.new(verts)
    bm.faces.ensure_lookup_table()
    # make sure the normal points down so the extrusion goes up cleanly
    if face.normal.z > 0:
        bmesh.ops.reverse_faces(bm, faces=[face])
    res = bmesh.ops.extrude_face_region(bm, geom=[face])
    top_verts = [g for g in res["geom"] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=(0, 0, height + EMBED), verts=top_verts)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    if bevel > 0:
        top_edges = [e for e in bm.edges if all(v.co.z > z0 + height - 1e-4 for v in e.verts)]
        bmesh.ops.bevel(bm, geom=top_edges, offset=min(bevel, height * 0.9), segments=bevel_segments,
                        profile=0.5, affect="EDGES", clamp_overlap=True)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _obj_from_bmesh(bm, name)


FOOT_GAP = 0.05       # footprints start this far above the back face: a face exactly coplanar
                      # with the back (z = 0) makes Blender's exact boolean leave holes. The gap
                      # is far below one layer, so the slicer prints it solid.


def footprint_from_outline(pts, name="footprint"):
    """Full-depth plate under an ornament that pokes outside the frame outline (z ≈ 0..3)."""
    return relief_from_outline(pts, FOOT_GAP + EMBED, PLATE_T - EMBED - FOOT_GAP + 0.05, bevel=0, name=name)


def tube(path, radius, z_base, height=None, n=10, name="tube"):
    """A thread along a polyline of (x, y) points, lying on the surface at z_base.
    Profile is a 'D': flat bottom (embedded EMBED into the surface), rounded top of the
    given height (defaults to radius). Width = 2 * radius."""
    if height is None:
        height = radius
    bm = bmesh.new()
    P = [Vector((x, y, 0.0)) for x, y in path]
    # profile loop: arc over the top from (+r, 0) to (-r, 0), then the flat embedded bottom
    prof = [(radius * math.cos(math.pi * i / n), height * math.sin(math.pi * i / n)) for i in range(n + 1)]
    prof += [(-radius, -EMBED), (radius, -EMBED)]
    rings = []
    for i, p in enumerate(P):
        if i == 0:
            d = (P[1] - P[0]).normalized()
        elif i == len(P) - 1:
            d = (P[-1] - P[-2]).normalized()
        else:
            d = ((P[i] - P[i - 1]).normalized() + (P[i + 1] - P[i]).normalized()).normalized()
        side = Vector((-d.y, d.x, 0.0))
        ring = [bm.verts.new(p + side * u + Vector((0, 0, z_base + v))) for u, v in prof]
        rings.append(ring)
    for a, b in zip(rings, rings[1:]):
        for i in range(len(a)):
            j = (i + 1) % len(a)
            bm.faces.new((a[i], a[j], b[j], b[i]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _obj_from_bmesh(bm, name)


def dome(center, rx, ry, height, z_base, name="dome", segments=32, rings=12):
    """Half-ellipsoid sitting on z_base (flat underside, embedded)."""
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, segments=segments, ring_count=rings,
                                         location=(center[0], center[1], z_base))
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = (rx, ry, height)
    bpy.ops.object.transform_apply(scale=True)
    # chop the lower half with a boolean against a big box
    bpy.ops.mesh.primitive_cube_add(size=1, location=(center[0], center[1], z_base - EMBED - 50))
    box = bpy.context.active_object
    box.scale = (100, 100, 100)
    bpy.ops.object.transform_apply(scale=True)
    difference(ob, box)
    return ob


def cutter_cylinder(center, r, z_top, depth, name="cut", vertices=32):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth + 1.0, vertices=vertices,
                                        location=(center[0], center[1], z_top - depth + (depth + 1.0) / 2))
    ob = bpy.context.active_object
    ob.name = name
    return ob


def cutter_box(center, sx, sy, z_top, depth, rot=0.0, name="cut"):
    """Rectangular cutter sx by sy, from z_top - depth up past z_top."""
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(center[0], center[1], z_top - depth + (depth + 1.0) / 2))
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = (sx, sy, depth + 1.0)
    ob.rotation_euler = (0.0, 0.0, rot)
    bpy.ops.object.transform_apply(scale=True, rotation=True)
    return ob


def place(ob, dx=0.0, dy=0.0, rot=0.0):
    """Rotate an object about the origin by rot (radians, about z) then move it by (dx, dy).
    Lets an ornament be built in local coordinates at the origin and dropped into place."""
    ob.rotation_euler = (0.0, 0.0, rot)
    ob.location = (dx, dy, 0.0)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True)
    return ob


def ellipse(center, rx, ry, n=32, rot=0.0):
    c, s = math.cos(rot), math.sin(rot)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        x, y = rx * math.cos(a), ry * math.sin(a)
        pts.append((center[0] + c * x - s * y, center[1] + s * x + c * y))
    return pts


# ---------------------------------------------------------------- booleans
def _apply_bool(target, other, op):
    mod = target.modifiers.new(name=op, type="BOOLEAN")
    mod.operation = op
    # Blender 4.5+/5.x "Manifold" solver: watertight output for watertight inputs. The
    # older "Exact" solver leaves boundary edges (holes) where operands meet the frame.
    try:
        mod.solver = "MANIFOLD"
    except TypeError:
        mod.solver = "EXACT"
    mod.object = other
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(other, do_unlink=True)


def union(target, other):
    _apply_bool(target, other, "UNION")


def difference(target, other):
    _apply_bool(target, other, "DIFFERENCE")


def transform_pts(pts, dx=0.0, dy=0.0, rot=0.0, sx=1.0, sy=1.0, mirror_x=False):
    c, s = math.cos(rot), math.sin(rot)
    out = []
    for x, y in pts:
        if mirror_x:
            x = -x
        x, y = x * sx, y * sy
        out.append((dx + c * x - s * y, dy + s * x + c * y))
    if mirror_x:
        out.reverse()      # keep counter-clockwise winding
    return out
