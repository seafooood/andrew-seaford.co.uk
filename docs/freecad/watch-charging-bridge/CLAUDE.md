# Watch Charging Bridge: agent notes

A 3D-printable charging stand shaped like a humpback stone bridge, for a **B9 band-style smartwatch**. The watch sits face-up in a curved cradle on top of the bridge (the crown), with its back resting on the magnetic charging plug. The mesh strap runs down both slopes between 3 mm walls. The charging cable runs out the back of the bridge.

The design has been printed and confirmed working. Treat the current dimensions as known-good, and change them only when the user asks.

## Files

| File | What it is |
|---|---|
| `watch-charging-bridge.scad` | **Source of truth.** Parametric OpenSCAD model. Edit this. |
| `watch-charging-bridge.stl` | Full bridge, exported with `part = "full"`. |
| `watch-charging-bridge-test.stl` | Crown-only fit test piece, exported with `part = "test"`. |
| `bridge-mockup.html` | Rev C design mockup (three.js + SVG drawings). Kept for reference only; it is **not** kept in sync with the .scad. It still shows the old cable route (a shaft down into the arch). |
| `*.jpeg`, `9530-600x600.jpg` | The user's caliper photos of the watch and plug, and the reference bridge photo. |

## How the model was made

1. **Measurements.** The user supplied caliper photos:
   - Charging plug: right-angle magnetic plug. Round head Ø6.28 × 5.94 thick, 10.11 long overall including the boot. Boot Ø4.7, cable Ø3.3. The metal contact circle is on the flat face of the head.
   - Watch body: 45.27 long × 19.98 wide × 4.1 thick. 8.22 total depth of the curved body, measured from the chord across the back ends to the top of the face. The back is concave along its length. The charging contact is centred across the width, 8 mm in from one end (the end opposite the CE mark).
   - Strap: 18 mm mesh.
2. **Mockup.** An HTML mockup went through revs A, B and C before any CAD. Rev A assumed a round watch with a flat landing. Rev B switched to the narrow band watch with a curved cradle. Rev C used the measured thickness and contact position.
3. **CAD.** The model is written in OpenSCAD 2021.01, the snap version at `/snap/bin/openscad` (CGAL backend, no manifold). It is built entirely from parameters, so every feature follows from the values at the top of the file.

## Geometry overview

Coordinates are in mm. **X** runs along the bridge, **Y** across it, and **Z** up. The bed is at z = 0. **−Y is the back**, where the cable leaves.

- **Deck profile `deck(x)`:** symmetric about x = 0.
  - `|x| ≤ ARC_END` (24): a circular arc of radius `WR`, which matches the watch back.
  - `ARC_END…RAMP_END` (24…58): a cubic Hermite blend down to `BASE_Z`. It is tangent to the arc at the top and flat at the bottom.
  - Beyond `RAMP_END`: flat at `BASE_Z` (12).
- **`WR` is derived, not set.** `SAG = W_DEPTH − W_T` and `WR = ((W_LEN/2)² + SAG²) / (2·SAG)`, which comes to about 64.2. Change the watch measurements, not `WR`.
- **`body()`:** the side profile (with a semicircular arch of radius `ARCH_R` sprung at `SPRING`) up to `deck(x) + WALL_H`, extruded across the full width `2·HW`.
- **`channel()`:** cuts away everything above `deck(x)` inside the walls. Half-width is `IN` (10, which gives a 20 mm strap channel), widened to `IN_C` (10.3, which gives a 20.6 mm cradle) over `|x| ≤ CRADLE`. The 0.3 mm per side clearance is needed because a 19.98 mm body jams in a 20.0 mm printed slot.
- **`pillars()`:** four corner posts at the ends. They are 6 long and 3.8 thick, stand 0.8 mm proud of the side faces, and have pyramid caps.
- **`charger_cut()`:**
  - Pocket and boot slot, placed at x = `CX` (`W_LEN/2 − W_CONTACT`, about 14.6) on the crown surface and tilted by `TH` (about 13.2°) so they sit square to the curve.
  - Pocket: Ø(`HEAD_D + FIT`), depth `HEAD_T − PROUD`, so the contact stands 0.24 mm proud.
  - Boot slot: `BOOT_D + 0.4` wide, running toward −Y.
  - Cable route: a trench `CABLE_D + 0.2` wide runs to the back face and through the back wall, then a groove runs down the back face into the arch opening. Every cable path is open from the top or the back, so the cable presses in and never has to be threaded (the USB plug on the other end won't fit through a hole).
- **`joints()`:** stone texture. Mortar grooves (`GROOVE_D` deep, `GROOVE_W` wide) in courses of `COURSE` height, with staggered joints every `BLOCK` along the length. Voussoir grooves go around the arch. It is applied to both outside faces only and kept clear of the pillars. The deck, cradle and inside faces of the walls stay smooth.
- **`part`:** `"test"` intersects the bridge with a box (`|x| ≤ TEST_X`, z ≥ `TEST_Z`) and drops the result to the bed, giving a 54 × 26 × 14 mm fit test piece.

## Editing workflow

1. Change parameters at the top of `watch-charging-bridge.scad`. Change module code only if the feature itself needs to change.
2. Export both STLs from the project folder:
   ```bash
   openscad -o watch-charging-bridge.stl watch-charging-bridge.scad
   openscad -D 'part="test"' -o watch-charging-bridge-test.stl watch-charging-bridge.scad
   ```
   Each takes a few seconds. Check the output reports `Volumes: 2` and no `ERROR`.
3. Check the bounding box. The full bridge should come out at 130 × 27.6 × 43:
   ```bash
   python3 -c "import re;v=[tuple(map(float,m)) for m in re.findall(r'vertex\s+(\S+)\s+(\S+)\s+(\S+)',open('watch-charging-bridge.stl').read())];[print(a,min(p[i] for p in v),max(p[i] for p in v)) for i,a in enumerate('xyz')]"
   ```
4. Render a preview PNG. **Snap OpenSCAD cannot write to `/tmp`**, so render into a folder under `$HOME` and copy the image out:
   ```bash
   D=~/snapshot-tmp; mkdir -p $D; cp watch-charging-bridge.stl $D/
   echo 'import("watch-charging-bridge.stl");' > $D/v.scad
   openscad -o $D/iso.png --imgsize=1100,700 --camera=0,0,20,40,0,-35,300 --colorscheme=Tomorrow $D/v.scad
   ```
   Look at the image, then delete `~/snapshot-tmp`.
5. For any change to a fit, suggest the user prints the test piece before the full bridge.

## Common changes

| Request | What to change |
|---|---|
| Plug too tight or loose | `FIT` (±0.1–0.2) |
| Watch binds in the cradle | `IN_C` (+0.1 widens the cradle by 0.2 mm) |
| Watch doesn't charge (contact too low) | `PROUD` up to about 0.4 |
| Different strap width | `IN` = strap/2 + 1 |
| Different watch | `W_LEN`, `W_DEPTH`, `W_T`, `W_CONTACT`, and `IN_C` (watch width/2 + 0.3). Check that `CRADLE` is longer than `W_LEN/2` plus a couple of mm for the strap hinges. |
| Smooth finish | `stone_texture = false` |
| Bigger or smaller bridge | `L`, `CROWN_Z`, `BASE_Z`, `ARCH_R`, `RAMP_END`. Keep `CROWN_Z` high enough above the arch (at least 10 mm of material under the pocket). |

## Gotchas

- **The deck profile is written three times.** The body, the channel and the cut all call `deck(x)`. If you change the profile, change `deck()` only, never the individual modules.
- **CGAL rejects coincident 2D edges.** OpenSCAD 2021 fails with "mesh is not closed" when 2D shapes share edges exactly. The joint pattern uses small overlaps (+0.1 / +0.2) to avoid this. Keep them if you edit `joints_2d()`.
- **Grooves must not reach into the pillars.** The groove cutters span y 12.4…14.4, and the pillars extend to 13.8. The pillar keep-out in `joints()` stops the grooves cutting internal voids.
- **The watch fits one way round.** Its charging end must sit over the pocket, on the +X side.
- **Print orientation.** Print upright, base on the bed, with no supports. The arch is a semicircle and every cut is open to the top or back.
