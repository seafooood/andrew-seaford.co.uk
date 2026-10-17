// Gothic buffet tag — Part A (frame) + Part B (L-clip). All dimensions in mm.
// How to use / adapt this file: README.md. Design rationale: docs/superpowers/specs/.
//
// Layers of Part A (see README):
//   part_a_plate()   structural: plate, keystone, socket, pawl, label recess  (reusable)
//   frame_relief2d() generic gothic mouldings and scrolls                    (reusable)
//   theme_relief2d() / theme_keystone2d()  the Halloween ornaments           (swap per design)
//
// view = "front"    Part A front, vertical
// view = "back"     Part A back, vertical (shows keystone socket)
// view = "a"        Part A print orientation (face up)
// view = "b"        Part B upright
// view = "assembly" both parts hung on a bowl rim (rim_t sets the rim thickness)
// view = "section"  exact cut through the clip centreline (CGAL, ~15 s)
// view = "print"    both parts laid out for printing
// view = "export_a"       Part A with the OpenSCAD theme ornaments, print orientation
// view = "export_a_blank" Part A with only the generic mouldings, for an ornament pass in Blender
// view = "export_b"       Part B lying on its side, print orientation

view = "front";
rim_t = 5;            // bowl rim thickness used in assembly/section views
$fn = 48;

// ---------- label ----------
label_w = 63.5;
label_h = 38.1;
label_clr = 0.25;      // per side
recess_d = 0.4;

// ---------- part A ----------
border_side = 10;
border_top = 13;
border_bot = 13;
plate_t = 3;
relief_h = 1.5;

plate_w = label_w + 2*label_clr + 2*border_side;   // 84.0
plate_h = label_h + 2*label_clr + border_top + border_bot; // 64.6

boss_w = 20;
boss_h = 8;            // how far the keystone rises above the plate's top edge
boss_lap = 2;          // overlap down into the top border for strength
boss_d = 12.5;         // total depth from the (flush) back face; 1.5 mm front wall
tunnel_w = 12.4;
tunnel_h = 3.8;        // 0.8 over the arm: lift-to-release headroom over the pawl
tunnel_depth = 11;     // = boss_d - 1.5
pawl_h = 0.5;

// ---------- part B ----------
// These values are tuned against a printed Part A whose socket entry measured
// 11.94 x 3.2 (first-layer squish of the nominal 12.4 x 3.8). Don't "correct" them
// back to nominal clearances without reprinting and re-testing.
arm_l = 13;
arm_w = 11.6;          // 0.5 clear of the printed socket width
arm_t = 3.1;           // near-zero play in the printed socket: the preload that makes it hold
leg_h = 25;
leg_t = 3;
tooth_pitch = 1.8;     // must exceed the 1.6 mm pawl length so the pawl nests in a groove
tooth_depth = 0.7;     // > pawl_h
tooth_start = 2.2;     // teeth run from here to the tip: (13 - 2.2) / 1.8 = 6 teeth
tip_chamfer = 0.5;     // lead-in on the arm tip
tongue_t = 1.2;        // teeth sit on a thin tongue that springs over the pawl
slot_h = 0.7;          // flex gap between tongue and the solid rail above
slot_x0 = 1.5;         // slot runs from here to the tip (open end)
fillet_r = 1.5;

// ---------- colours ----------
pla = "#2e2e2e";     // black PLA
pla_hi = "#5a5a5a";  // relief drawn lighter in renders so it reads (same PLA when printed)
show_label = true;   // cream placeholder label in the recess (mockup only)
label_text = "Pumpkin Soup";
bowl_col = [0.85, 0.9, 0.95, 0.5];

// =====================================================================
// 2D ornament silhouettes
// =====================================================================

// Bat, wingspan ~ 2*span, facing viewer, origin at body centre.
module bat2d(span = 12) {
    s = span / 12;
    // half wing (right side), scalloped trailing edge
    half = [[0, 3.2], [1.2, 3.6], [2.2, 4.0], [3.5, 5.0], [5.5, 5.6], [8, 5.4],
            [10.5, 4.6], [12, 3.2],
            [11, 1.6], [9.8, 0.2], [8.8, 1.2], [7.6, -0.6], [6.4, 0.8],
            [5.2, -1.4], [4.0, -0.2], [2.6, -2.2], [1.4, -1.4], [0, -2.8]];
    scale(s) {
        polygon(half);
        mirror([1, 0]) polygon(half);
        // body
        scale([1, 1.6]) circle(d = 3.2, $fn = 24);
        // head + ears
        translate([0, 2.4]) circle(d = 2.6, $fn = 24);
        translate([-0.9, 3.2]) rotate(15) polygon([[-0.7, 0], [0.7, 0], [0, 1.8]]);
        translate([0.9, 3.2]) rotate(-15) polygon([[-0.7, 0], [0.7, 0], [0, 1.8]]);
    }
}

// Jack-o'-lantern, ~d wide, origin at centre. face=true cuts the face out.
module pumpkin2d(d = 13, face = true) {
    s = d / 13;
    scale(s) difference() {
        union() {
            // ribbed body: overlapping lobes
            for (x = [-3.6, -1.8, 0, 1.8, 3.6])
                translate([x, 0]) scale([1, 0.88]) circle(d = 7.6 - abs(x)*0.5, $fn = 40);
            // stem
            translate([0, 4.6]) rotate(12) square([1.6, 2.6], center = true);
        }
        if (face) {
            // eyes
            translate([-2.1, 1.0]) polygon([[-1.2, -0.8], [1.2, -0.8], [0, 1.2]]);
            translate([ 2.1, 1.0]) polygon([[-1.2, -0.8], [1.2, -0.8], [0, 1.2]]);
            // nose
            translate([0, -0.2]) polygon([[-0.6, -0.5], [0.6, -0.5], [0, 0.5]]);
            // zig-zag mouth
            polygon([[-3.2, -1.6], [3.2, -1.6], [2.4, -2.6], [1.6, -1.9], [0.8, -2.9],
                     [0, -2.0], [-0.8, -2.9], [-1.6, -1.9], [-2.4, -2.6]]);
        }
    }
}

// One "C" scroll, ~L long. Used in rows along the borders.
module scroll2d(L = 8) {
    s = L / 8;
    scale(s) {
        difference() {
            translate([2, 0]) circle(r = 2.2, $fn = 32);
            translate([2, 0]) circle(r = 1.2, $fn = 32);
            translate([2, -3]) square([3, 6]);
        }
        difference() {
            translate([6, 0]) circle(r = 2.2, $fn = 32);
            translate([6, 0]) circle(r = 1.2, $fn = 32);
            translate([3, -3]) square([3, 6]);
        }
        translate([4, 0]) circle(r = 0.7, $fn = 16);
    }
}

// Row of scrolls with beads between, centred on origin, along +X.
module scroll_row2d(len, L = 8) {
    n = floor(len / L);
    for (i = [0 : n-1])
        translate([-len/2 + i*L + L/2 - 4*(L/8), 0]) scroll2d(L);
}

// =====================================================================
// Part A outline & relief
// =====================================================================

// Outer 2D silhouette of the plate: rectangle with scalloped edge,
// bulged corners and a crest at top centre.
module plate_outline2d() {
    w = plate_w; h = plate_h;
    union() {
        offset(r = 4) offset(delta = -4) square([w, h], center = true);
        // corner bulges
        for (sx = [-1, 1], sy = [-1, 1])
            translate([sx*(w/2 - 4), sy*(h/2 - 4)]) circle(r = 7.5, $fn = 40);
        // mid-side bulges (left/right)
        for (sx = [-1, 1])
            translate([sx*w/2, label_cy]) scale([1, 2.6]) circle(r = 3.6, $fn = 40);
        // bottom-centre bulge
        translate([0, -h/2]) scale([2.8, 1]) circle(r = 3.6, $fn = 40);
        // keystone footprint at top centre (solid block, see part_a_plate)
        translate([0, h/2 + boss_h/2 - boss_lap/2])
            offset(r = 1.5) offset(delta = -1.5) square([boss_w, boss_h + boss_lap], center = true);
    }
}

// Window centre offset (label is centred between top and bottom border)
label_cy = (border_bot - border_top) / 2;

module recess2d() {
    translate([0, label_cy])
        square([label_w + 2*label_clr, label_h + 2*label_clr], center = true);
}

// ---- generic frame mouldings (reusable across designs) ----
module frame_relief2d() {
    w = plate_w; h = plate_h;
    // inner moulding ring around the recess
    translate([0, label_cy]) difference() {
        offset(r = 1.8) recess2d_local();
        offset(r = 0.5) recess2d_local();
    }
    // outer bead ring following the outline, plus a thin second moulding line
    difference() { plate_outline2d(); offset(delta = -1.4) plate_outline2d(); }
    difference() { offset(delta = -3.0) plate_outline2d(); offset(delta = -3.8) plate_outline2d(); }
    // scroll rows top & bottom, between the corner ornaments
    translate([0, h/2 - border_top/2 - 1.2]) scroll_row2d(w - 46, 7.5);
    translate([0, -h/2 + border_bot/2 + 0.8]) scroll_row2d(w - 46, 7.5);
    // small scrolls in the side bulges
    for (sx = [-1, 1])
        translate([sx*(w/2 - border_side/2 + 0.6), label_cy]) rotate(90) scroll_row2d(15, 7.5);
}

// ---- theme ornaments: Halloween (swap this module for a different design) ----
// Anything placed outside plate_outline2d() gets the full plate under it automatically.
module theme_relief2d() {
    w = plate_w; h = plate_h;
    // bats: top corners, wings break past the outline
    for (sx = [-1, 1])
        translate([sx*(w/2 - 8), h/2 - 3]) rotate(sx * -18) bat2d(15);
    // pumpkins: bottom corners, sitting proud of the outline, plus a small one at bottom centre
    for (sx = [-1, 1])
        translate([sx*(w/2 - 7.5), -h/2 + 5.5]) pumpkin2d(17);
    translate([0, -h/2 + 1.5]) pumpkin2d(11);
}
// Ornament on the keystone's front face. Keep it inside the 20 x 10 face
// (it is 9.5 mm up in the air, so nothing may overhang the block).
module theme_keystone2d() {
    translate([0, boss_y0 + boss_ht/2 - 0.3]) bat2d(14);
}

// Everything raised above the plate front face, as 2D.
module relief2d(theme = true) {
    frame_relief2d();
    if (theme) theme_relief2d();
}
module recess2d_local() {
    square([label_w + 2*label_clr, label_h + 2*label_clr], center = true);
}

// Part A in print orientation: flat back on z=0, front face up. Plate to z=3,
// relief to 4.5, keystone to 12.5 (+1.5 for its ornament).
boss_y0 = plate_h/2 - boss_lap;                 // bottom of keystone (plate coords)
boss_ht = boss_h + boss_lap;                    // keystone height
tunnel_y0 = boss_y0 + (boss_ht - tunnel_h)/2;   // tunnel floor (plate coords)

module part_a_plate(theme = true) {
    difference() {
        union() {
            // plate, including the footprint of any ornament that breaks the outline
            linear_extrude(plate_t) union() { plate_outline2d(); relief2d(theme); }
            // keystone: sits on the top edge, flush with the back (z=0), rises to boss_d
            translate([-boss_w/2, boss_y0, 0]) cube([boss_w, boss_ht, boss_d]);
        }
        // label recess
        translate([0, 0, plate_t - recess_d]) linear_extrude(recess_d + 1) recess2d();
        // blind tunnel entering from the back face
        translate([-tunnel_w/2, tunnel_y0, -0.01]) cube([tunnel_w, tunnel_h, tunnel_depth]);
    }
    // pawl ridge on tunnel floor, 1.5 mm in from the entry; vertical face inward
    translate([0, tunnel_y0, 1.5])
        rotate([0, -90, 0])
            linear_extrude(tunnel_w - 0.4, center = true)
                polygon([[-1.2, 0], [0.4, 0], [0.4, pawl_h]]);
}
module part_a_relief(theme = true) {
    translate([0, 0, plate_t]) linear_extrude(relief_h) relief2d(theme);
    if (theme) translate([0, 0, boss_d]) linear_extrude(relief_h) theme_keystone2d();
}
module part_a_body() {
    color(pla) part_a_plate();
    color(pla_hi) part_a_relief();
}

// Mockup-only placeholder sticker sitting in the recess.
module label_placeholder() {
    if (show_label) {
        color("#efe6d2") translate([0, 0, plate_t - recess_d]) linear_extrude(recess_d - 0.05)
            offset(delta = -0.3) recess2d();
        color("#3a2a22") translate([0, label_cy, plate_t])
            linear_extrude(0.1) {
                translate([0, 3]) text(label_text, size = 6.5, halign = "center", valign = "center", font = "Liberation Serif:style=Bold");
                translate([0, -7]) text("vegan  \u00b7  gluten free", size = 3.2, halign = "center", valign = "center", font = "Liberation Sans");
            }
    }
}

// Part A oriented vertically as it hangs: front face toward -Y, top at +Z.
module part_a_vertical() {
    rotate([90, 0, 0]) { part_a_body(); label_placeholder(); }
}

// =====================================================================
// Part B — L-clip
// =====================================================================

// Profile in the XZ plane (X along arm, Z up). Arm runs from x=0 (leg) to x=arm_l,
// teeth on the underside of the arm; leg drops from the corner.
module part_b_profile() {
    difference() {
        union() {
            square([arm_l, arm_t]);                          // arm
            translate([-leg_t, -leg_h]) square([leg_t, leg_h + arm_t]); // leg
            // inside fillet
            translate([0, 0]) difference() {
                square([fillet_r, fillet_r]) ;
                translate([fillet_r, fillet_r]) circle(r = fillet_r, $fn = 24);
            }
        }
        // ratchet teeth: vertical face toward the tip, ramp toward the leg,
        // so the pawl slides over on insertion and locks on withdrawal
        for (x = [tooth_start : tooth_pitch : arm_l - tooth_pitch + 0.01])
            polygon([[x, -0.01], [x + tooth_pitch, -0.01], [x + tooth_pitch, tooth_depth]]);
        // flex slot: tongue below, rail above
        translate([slot_x0, tongue_t]) square([arm_l - slot_x0 + 0.01, slot_h]);
        // lead-in chamfers on the tip
        polygon([[arm_l + 0.01, arm_t + 0.01], [arm_l - tip_chamfer, arm_t + 0.01], [arm_l + 0.01, arm_t - tip_chamfer]]);
        polygon([[arm_l + 0.01, -0.01], [arm_l - tip_chamfer, -0.01], [arm_l + 0.01, tip_chamfer]]);
    }
}

module part_b() {
    rotate([90, 0, 0]) linear_extrude(arm_w, center = true) part_b_profile();
}

// =====================================================================
// Bowl rim stub for context (curved wall, rim just under the boss)
// =====================================================================
rim_z = tunnel_y0 - 1.0;            // rim top sits just under the arm
bowl_r = 70;
module bowl_stub(t = rim_t) {
    color(bowl_col)
        translate([0, bowl_r, rim_z - 60])
            difference() {
                cylinder(r = bowl_r, h = 60, $fn = 160);
                translate([0, 0, -1]) cylinder(r = bowl_r - t, h = 62, $fn = 160);
                translate([-200, 0, -1]) cube([400, 200, 62]);   // keep the near half only
            }
}

// =====================================================================
// Assembly
// =====================================================================
// Part A hangs with its front toward -Y and its flush back face at y = 0.
// Bowl wall occupies y in [0, t]. Part B's leg sits just beyond it.
tunnel_floor_z = tunnel_y0;

module part_b_placed(t = rim_t) {
    translate([0, t, tunnel_floor_z]) rotate([0, 0, -90]) part_b();
}
module assembly(t = rim_t, show_bowl = true) {
    part_a_vertical();
    color(pla) part_b_placed(t);
    if (show_bowl) bowl_stub(t);
}

// True 2D section through the clip centreline (plane x = 0), drawn in the
// YZ plane as a thin slab so it can be rendered top-down. Uses CGAL, so it
// is slow (a minute or so) but exact. Y = out from bowl, Z = up.
cut_frame = "#3a3a3a"; cut_clip = "#8a8a8a"; cut_bowl = "#9fb4c4";
module slice(c) {
    color(c) linear_extrude(1)
        projection(cut = true) rotate([0, 90, 0]) children();  // x -> -z, cut at z=0
}
module section_view(t = rim_t) {
    // rotate([0,90,0]) maps (x,y,z) -> (z, y, -x); projection keeps (X,Y) = (z, y)
    // so the 2D drawing has plot-x = world z (up) and plot-y = world y. Rotate so
    // world y runs left-to-right and world z runs up.
    mirror([1, -1, 0]) {   // swap axes: plot-x = world y, plot-y = world z
        slice(cut_frame) part_a_plate_vertical();
        slice(cut_clip) part_b_placed(t);
        slice(cut_bowl) bowl_stub(t);
    }
}
module part_a_plate_vertical() {
    rotate([90, 0, 0]) { part_a_plate(); part_a_relief(); }
}

// =====================================================================
// Views
// =====================================================================
if (view == "front" || view == "back") part_a_vertical();
else if (view == "a") { part_a_body(); label_placeholder(); }
else if (view == "b") color(pla) part_b();
else if (view == "assembly") assembly(rim_t, true);
else if (view == "section") section_view(rim_t);
// STL export orientations: back of Part A on z=0, Part B lying on its side on z=0
else if (view == "export_a") { part_a_plate(); part_a_relief(); }
else if (view == "export_a_blank") { part_a_plate(false); part_a_relief(false); }
else if (view == "export_b") translate([0, 0, arm_w/2]) rotate([-90, 0, 0]) part_b();
else if (view == "print") {
    part_a_body();
    color(pla) translate([0, -plate_h/2 - 25, arm_w/2]) rotate([-90, 0, 0]) part_b();
}
