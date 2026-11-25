// Tree shelf clamp - one half (print 2). Units: mm.
// Modelled in print orientation: shelf-side face on the bed (z=0).
$fn=128;
ri=40; ro=50; H=30;             // inner radius, outer radius, height
fl_t=5; fl_out=18;              // bolt-together flange: thickness, length past outer radius
tab_out=10; tab_t=5; tab_w=18;  // L-bracket tab: projection, thickness, width
tab_angs=[0,65,-65];
grip_ang=32;                    // grip bolt angle from centre line
grip_z=H-12;                    // grip bolt height from bed (12 mm below shelf face in use)
bolt_d=6.6;                     // M6 clearance
nut_af=10.4; nut_t=5.6;         // M6 nut pocket (10 mm AF + clearance)
screw_d=4.5;                    // wood screw clearance

module ring(){
  intersection(){
    difference(){ cylinder(r=ro,h=H); translate([0,0,-1]) cylinder(r=ri,h=H+2); }
    translate([0,-200,-1]) cube([400,400,H+2]);
  }
}
module tab(){
  translate([ro-2,-tab_w/2,0]) cube([tab_out+2,tab_w,tab_t]);
  // 45 deg gusset (self-supporting in this orientation)
  hull(){
    translate([ro-2,-tab_w/2,tab_t-0.01]) cube([tab_out+2,tab_w,0.01]);
    translate([ro-2,-tab_w/2,tab_t+tab_out]) cube([0.01,tab_w,0.01]);
  }
}
difference(){
  union(){
    ring();
    for(s=[1,-1]) translate([0, s>0?ri:-(ro+fl_out), 0]) cube([fl_t, ro+fl_out-ri, H]);
    for(a=tab_angs) rotate(a) tab();
  }
  for(s=[1,-1]) translate([-1, s*(ro+fl_out/2), H/2]) rotate([0,90,0]) cylinder(d=bolt_d,h=fl_t+2,$fn=48);
  for(s=[1,-1]) rotate(s*grip_ang) translate([0,0,grip_z]) {
    translate([ri-5,0,0]) rotate([0,90,0]) cylinder(d=bolt_d,h=ro-ri+20,$fn=48);
    // hex pocket, vertex pointing up for clean bridging
    translate([ri-1,0,0]) rotate([0,90,0]) cylinder(d=nut_af/cos(30),h=nut_t+1,$fn=6);
  }
  for(a=tab_angs) rotate(a) translate([ro+tab_out/2,0,-1]) cylinder(d=screw_d,h=tab_t+tab_out+2,$fn=32);
}
