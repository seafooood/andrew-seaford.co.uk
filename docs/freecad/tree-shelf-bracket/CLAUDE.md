# Tree Shelf Clamp: project brief for agents

This file gets an agent up to speed on the project so that it can change the model.

## What the part is

- It is a two-piece clamp that grips a vertical tree trunk and holds a wooden shelf on top of it.
- The two halves are **identical**. You print the same STL twice and turn one half 180° about the trunk axis.
- The idea came from the centre clamp of a Christmas-tree train set, which uses wing screws to grip the trunk.
- The user drew the brief by hand (a top view and a side view). The user approved the concept renders and then the final STL.

## Files

| File | Purpose |
|---|---|
| `tree_shelf_clamp.scad` | The source of truth. This is the parametric OpenSCAD model of one half. |
| `tree_shelf_clamp_half.stl` | The exported print file. Regenerate it after every change to the `.scad` file. |
| `tree_shelf_clamp_half.png` | The preview render of the final part. |
| `concept/concept.scad` | The concept model with modes for the assembly, the shelf and the print bed. It is for pictures only, not for printing. |
| `concept/*.png` | The concept renders that the user approved. |
| `PRINTABLES.md` | The description for the Printables upload. |

## Coordinate system and orientation

- The model is in the **print orientation**. The shelf-side face is on the bed at `z=0`.
- When the clamp is in use, the part is the other way up. The `z=0` face touches the underside of the shelf.
- The split plane is `x=0`. The half ring is on the `+x` side.
- The trunk axis is the `z` axis.
- Angles are measured from the `+x` axis (the middle of the half) around `z`.

## Features and parameters

All units are mm.

| Feature | Parameters | Value | Notes |
|---|---|---|---|
| Half ring | `ri`, `ro`, `H` | 40, 50, 30 | This gives an 80 mm bore, a 100 mm outside diameter and a 10 mm wall. |
| Join flanges (one at each end) | `fl_t`, `fl_out` | 5, 18 | Each flange is a plate on the split plane that reaches 18 mm past `ro`. It has one M6 hole along `x`, centred at `y=±(ro+fl_out/2)`, `z=H/2`. |
| L-bracket tabs (3) | `tab_out`, `tab_t`, `tab_w`, `tab_angs` | 10, 5, 18, `[0,65,-65]` | Each tab is flush with the `z=0` face and has a 45° gusset. The gusset prints without supports in this orientation. |
| Tab screw holes | `screw_d` | 4.5 | The holes are vertical, for wood screws into the shelf. |
| Grip bolt holes (2) | `grip_ang`, `grip_z`, `bolt_d` | ±32°, `H-12`, 6.6 | The holes point at the centre. In use they sit 12 mm below the shelf face. |
| Captive nut pockets (2) | `nut_af`, `nut_t` | 10.4, 5.6 | The hex pockets open on the **inner** face for M6 nuts. One point of the hex faces `±z` so that the roof prints without supports. |

## How the clamp works

1. An M6 nut goes into each inner pocket.
2. An M6 bolt goes in from the outside, screws through the nut and presses on the trunk.
3. A wing nut on the outside locks the bolt.
4. Two M6 bolts hold the halves together through the flanges.
5. Six wood screws hold the tabs to the underside of the shelf.

## Design decisions and why

- **Identical halves:** you only need one STL. Each half has rotational symmetry about the trunk, so the flanges meet face to face.
- **Upside-down printing:** the tabs and the shelf face are on the bed, so the part needs no supports. Any new feature must stay printable in this orientation. For example, use overhangs of 45° or less, and use a point-up hex or teardrop shape for horizontal holes.
- **Nuts on the inner face:** this follows the user's sketch. The user was offered pockets on the outer face and did not ask for them.
- **The two long arms on the right of the sketch:** these were an earlier idea and are not part of the design.
- **Tab angles of ±65°:** these leave space for the wing nuts at ±32°.

## Known limits and open points

- The part has not been printed or tested yet.
- The 80 mm bore is large. A thin trunk depends on long grip bolts. To get a smaller bore, change `ri` and `ro` together and keep the wall about 10 mm thick.
- The bolt lengths in the hardware list are estimates, and they depend on the trunk diameter.
- The grip bolt holes must not touch a tab gusset. If you change `tab_angs`, `tab_w` or `grip_ang`, check the clearance.

## How to make a change

1. Edit the parameters or the geometry in `tree_shelf_clamp.scad`.
2. Export the STL:
   `openscad -o tree_shelf_clamp_half.stl tree_shelf_clamp.scad`
3. Make sure that the output says `Simple: yes`. This means the solid is closed and valid.
4. Render a preview:
   `openscad -o tree_shelf_clamp_half.png --imgsize=1400,1000 --colorscheme=Tomorrow --camera=25,0,12,55,0,210,260 tree_shelf_clamp.scad`
5. Open the PNG and check the change by eye.
6. Show the user a render before you make a large change to the geometry. The user wants to approve the design before the final CAD.
7. Update this file and `PRINTABLES.md` if any size or hardware changes.

## Notes on the environment

- OpenSCAD is installed at `/snap/bin/openscad`. Blender is also available.
- FreeCAD and Python matplotlib are not installed.
