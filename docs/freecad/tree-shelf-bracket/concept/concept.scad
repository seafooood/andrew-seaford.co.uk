// CONCEPT ONLY - for checking the brief. Units: mm. Z up = shelf side (as used).
$fn=96;
ri=40; ro=50; H=30;            // inner radius, outer radius, height
fl_t=5; fl_out=18;             // bolt-together flange: thickness, length past outer radius
tab_out=10; tab_t=5; tab_w=18; // L-bracket tab: projection, thickness, width
grip_ang=32; grip_z=12;        // grip bolt angle from centre line, height
tab_angs=[0,65,-65];
part = is_undef(part) ? "assembly" : part;

module half(){
  difference(){
    union(){
      // half ring
      intersection(){
        difference(){ cylinder(r=ro,h=H); translate([0,0,-1]) cylinder(r=ri,h=H+2); }
        translate([0,-200,-1]) cube([400,400,H+2]);
      }
      // flanges on split plane
      for(s=[1,-1]) translate([0, s>0?ri:-(ro+fl_out), 0]) cube([fl_t, ro+fl_out-ri, H]);
      // L-bracket tabs flush with top + 45deg gusset
      for(a=tab_angs) rotate(a) {
        translate([ro-2,-tab_w/2,H-tab_t]) cube([tab_out+2,tab_w,tab_t]);
        hull(){
          translate([ro-2,-tab_w/2,H-tab_t]) cube([0.1,tab_w,tab_t]);
          translate([ro-2,-tab_w/2,H-tab_t-tab_out]) cube([0.1,tab_w,0.1]);
          translate([ro+tab_out-0.1,-tab_w/2,H-tab_t]) cube([0.1,tab_w,0.1]);
        }
      }
    }
    // flange bolt holes M6
    for(s=[1,-1]) translate([-1, s*(ro+fl_out/2), H/2]) rotate([0,90,0]) cylinder(d=6.5,h=fl_t+2);
    // grip bolt holes + M6 captive nut pockets (inner face)
    for(s=[1,-1]) rotate(s*grip_ang) translate([0,0,grip_z]) {
      rotate([0,90,0]) cylinder(d=6.5,h=ro+5);
      translate([ri-1,0,0]) rotate([0,90,0]) rotate(30) cylinder(d=11.6,h=6.2,$fn=6);
    }
    // screw holes in tabs
    for(a=tab_angs) rotate(a) translate([ro+tab_out/2,0,0]) cylinder(d=4.5,h=H+2);
  }
}
module nuts(){ color("saddlebrown") for(s=[1,-1]) rotate(s*grip_ang) translate([ri,0,grip_z]) rotate([0,90,0]) rotate(30) difference(){cylinder(d=11.5,h=5,$fn=6); translate([0,0,-1])cylinder(d=6,h=7);} }
module wingbolts(){ color("silver") for(s=[1,-1]) rotate(s*grip_ang) translate([0,0,grip_z]) {
  translate([ri-8,0,0]) rotate([0,90,0]) cylinder(d=6,h=60);
  translate([ro+12,0,0]) rotate([0,90,0]) { cylinder(d=12,h=6); hull(){ translate([0,-14,3]) cylinder(d=4,h=1); translate([0,14,3]) cylinder(d=4,h=1); translate([-6,0,3]) cylinder(d=3,h=1);} }
}}
module trunk(){ color("peru",0.5) translate([0,0,-40]) cylinder(r=30,h=H+80); }
module shelf(){ color("burlywood",0.35) translate([-150,-150,H]) difference(){ cube([300,300,18]); translate([150,150,-1]) cylinder(r=52,h=20); translate([150-1,0,-1]) cube([2,150,20]);} }

if(part=="half"){ color("orange") half(); nuts(); }
if(part=="print"){ color("orange") translate([0,0,H]) mirror([0,0,1]) half(); color("lightgrey") translate([-40,-90,-1]) cube([160,180,1]); }
if(part=="assembly"){ color("orange") half(); color("darkorange") rotate(180) half(); nuts(); rotate(180) nuts(); wingbolts(); rotate(180) wingbolts(); trunk();
  color("silver") for(s=[1,-1]) translate([-25, s*(ro+fl_out/2), H/2]) rotate([0,90,0]) cylinder(d=6,h=50); }
if(part=="shelf"){ color("orange") half(); color("darkorange") rotate(180) half(); trunk(); shelf(); }
