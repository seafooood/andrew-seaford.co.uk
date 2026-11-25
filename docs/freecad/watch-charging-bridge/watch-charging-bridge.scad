// Watch Charging Bridge — rev C
// Humpback stone bridge that holds a B9 band watch face-up on a magnetic
// charging plug. All dimensions in mm. X = along the bridge, Y = across, Z = up.
// The back of the bridge (where the cable leaves) is the -Y side.

/* [Bridge] */
L          = 65;     // half length (overall 130)
HW         = 13;     // half width (overall 26)
BASE_Z     = 12;     // deck height at the ends
CROWN_Z    = 40;     // deck height at the crown
ARC_END    = 24;     // crown curve runs |x| <= ARC_END
RAMP_END   = 58;     // ramps reach BASE_Z here
ARCH_R     = 18;     // arch radius
SPRING     = 6;      // arch springing height

/* [Walls / channel] */
WALL_H     = 3;      // wall height above the deck
IN         = 10;     // half channel width on the ramps (20 mm for 18 mm strap)
IN_C       = 10.3;   // half cradle width at the crown (20.6 mm for 19.98 mm body)
CRADLE     = 25;     // cradle runs |x| <= CRADLE
PIL_H      = 9;      // corner pillar height above BASE_Z

/* [Watch (B9)] */
W_LEN      = 45.27;
W_DEPTH    = 8.22;   // chord of back ends to top of face
W_T        = 4.1;    // body thickness
W_CONTACT  = 8;      // charging end to contact centre

/* [Charging plug] */
HEAD_D     = 6.28;
HEAD_T     = 5.94;
BOOT_D     = 4.7;
CABLE_D    = 3.3;
PROUD      = 0.24;   // contact face stands this far above the crown
FIT        = 0.3;    // clearance on the head diameter

/* [Output] */
part = "full";       // "full" = whole bridge, "test" = crown-only fit test piece
TEST_Z = 29;         // test piece is cut flat at this height
TEST_X = 27;         // test piece runs |x| <= TEST_X

/* [Finish] */
stone_texture = true;
GROOVE_D   = 0.6;    // mortar joint depth
GROOVE_W   = 0.8;    // mortar joint width
COURSE     = 5;      // stone course height
BLOCK      = 11;     // stone block length

$fn = 64;

// ---- derived ----
SAG  = W_DEPTH - W_T;                               // back curve depth
WR   = (pow(W_LEN/2,2) + SAG*SAG) / (2*SAG);        // back radius (~64.2)
WCZ  = CROWN_Z - WR;                                // crown circle centre z
CX   = W_LEN/2 - W_CONTACT;                         // plug x (~14.6)
TH   = asin(CX/WR);                                 // plug tilt (~13.2 deg)
PZ   = WCZ + sqrt(WR*WR - CX*CX);                   // crown z at plug
POCKET_D = HEAD_D + FIT;
POCKET_H = HEAD_T - PROUD;
BOOT_W   = BOOT_D + 0.4;
SLOT_W   = CABLE_D + 0.2;

function arcZ(x) = WCZ + sqrt(WR*WR - x*x);
YA = arcZ(ARC_END);
SA = -ARC_END / sqrt(WR*WR - ARC_END*ARC_END);
function herm(a) = let(D = RAMP_END - ARC_END, t = (a - ARC_END)/D)
    (2*pow(t,3) - 3*t*t + 1)*YA + (pow(t,3) - 2*t*t + t)*D*SA + (-2*pow(t,3) + 3*t*t)*BASE_Z;
function deck(x) = let(a = abs(x)) a <= ARC_END ? arcZ(a) : a >= RAMP_END ? BASE_Z : herm(a);

// extrude a polygon drawn in the XZ plane across Y
module xz(w, y0 = 0) translate([0, y0, 0]) rotate([90, 0, 0]) linear_extrude(height = w, center = true) children();

// ---- body: side profile with arch, up to the wall tops ----
module body() {
    arch = [for (a = [180 : -3 : 0]) [ARCH_R*cos(a), SPRING + ARCH_R*sin(a)]];
    top  = [for (x = [L : -0.5 : -L]) [x, deck(x) + WALL_H]];
    xz(2*HW) polygon(concat([[-L, 0], [-ARCH_R, 0]], arch, [[ARCH_R, 0], [L, 0]], top));
}

// ---- strap channel and watch cradle ----
module channel_2d(x0, x1) {
    n = ceil((x1 - x0)/0.5);
    polygon(concat([for (i = [0 : n]) let(x = x0 + i*(x1 - x0)/n) [x, deck(x)]],
                   [for (i = [n : -1 : 0]) let(x = x0 + i*(x1 - x0)/n) [x, deck(x) + 20]]));
}
module channel() {
    xz(2*IN)   channel_2d(-L - 1, L + 1);
    xz(2*IN_C) channel_2d(-CRADLE, CRADLE);
}

// ---- corner pillars with pyramid caps ----
module pillars() {
    for (sx = [-1, 1], sy = [-1, 1]) {
        x0 = sx > 0 ? L - 6 : -L;
        y0 = sy > 0 ? IN : -HW - 0.8;
        translate([x0, y0, 0]) {
            cube([6, HW + 0.8 - IN, BASE_Z + PIL_H]);
            hull() {
                translate([0, 0, BASE_Z + PIL_H]) cube([6, HW + 0.8 - IN, 0.01]);
                translate([3, (HW + 0.8 - IN)/2, BASE_Z + PIL_H + 2.4]) cube(0.01, center = true);
            }
        }
    }
}

// ---- charger pocket, boot slot and cable route to the back ----
module charger_cut() {
    translate([CX, 0, PZ]) rotate([0, TH, 0]) {
        translate([0, 0, -POCKET_H]) cylinder(d = POCKET_D, h = POCKET_H + 8);
        translate([-BOOT_W/2, -9, -POCKET_H]) cube([BOOT_W, 9, POCKET_H + 8]);
    }
    // trench from the boot to the back face, through the back wall
    translate([CX - SLOT_W/2, -HW - 1, PZ - POCKET_H]) cube([SLOT_W, HW + 1 - 6, 20]);
    // groove down the back face into the arch mouth
    translate([CX - SLOT_W/2, -HW - 1, 0]) cube([SLOT_W, SLOT_W + 1.2, PZ + 1]);
}

// ---- stone joints on the outside faces ----
module joints_2d() {
  union() {
    difference() {
        union() {
            for (k = [1 : ceil((CROWN_Z + WALL_H)/COURSE)]) {
                translate([-L - 1, k*COURSE - GROOVE_W/2]) square([2*L + 2, GROOVE_W]);
            }
            for (k = [0 : ceil((CROWN_Z + WALL_H)/COURSE)], n = [-7 : 7]) {
                translate([n*BLOCK + (k % 2)*BLOCK/2 - GROOVE_W/2, k*COURSE - 0.1]) square([GROOVE_W, COURSE + 0.2]);
            }
        }
        translate([0, SPRING]) circle(r = ARCH_R + 4.4);
    }
    // voussoirs around the arch
    translate([0, SPRING]) {
        difference() {
            circle(r = ARCH_R + 4.5);
            circle(r = ARCH_R + 4.4 - GROOVE_W);
            translate([-40, -40]) square([80, 40]);
        }
        for (a = [20 : 20 : 160]) rotate(a) translate([ARCH_R - 1, -GROOVE_W/2]) square([5.4, GROOVE_W]);
    }
  }
}
module joints() {
    for (s = [-1, 1])
        intersection() {
            xz(2, s*(HW + 1 - GROOVE_D)) joints_2d();
            // keep clear of the pillars
            union() {
                translate([-L + 6, -50, -1]) cube([2*L - 12, 100, 100]);
                translate([-L - 2, -50, -1]) cube([2*L + 4, 100, BASE_Z + 1]);
            }
        }
}

// ---- assembly ----
module bridge() {
    difference() {
        union() { body(); pillars(); }
        channel();
        charger_cut();
        if (stone_texture) joints();
    }
}

if (part == "test") {
    // top of the crown only, dropped to the bed: checks the plug pocket,
    // cable slots and watch cradle fit in a short print
    translate([0, 0, -TEST_Z]) intersection() {
        bridge();
        translate([-TEST_X, -HW - 2, TEST_Z]) cube([2*TEST_X, 2*HW + 4, 30]);
    }
} else {
    bridge();
}
