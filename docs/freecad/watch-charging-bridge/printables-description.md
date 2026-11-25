# Stone Bridge Charging Stand for B9 Smartwatch

A little humpback stone bridge that holds your B9 band smartwatch while it charges. The watch sits face-up on top of the bridge with its back on the magnetic charger, and the strap drapes down both sides. The charging cable tucks away out the back.

I designed it around my own watch and its charging cable, and it works perfectly.

## Features

- **Curved cradle** shaped to the watch's curved back, so the body sits snugly and doesn't rock.
- **Charger built in:** the magnetic plug pushes into a pocket at the top of the bridge, lined up under the watch's charging contact, with the contact face sitting just above the surface. Set the watch down and it snaps on.
- **Strap channel:** 3 mm walls either side keep the 18 mm strap in place on the slopes.
- **Hidden cable:** the cable presses into a slot that runs out through the back wall and down the back face into the arch, so you don't need to thread the USB plug through anything.
- **Stone finish:** mortar joints on the sides and around the arch, and pointed corner pillars. The surfaces the watch touches are smooth.
- **No supports needed:** it prints standing upright.

## What you need

- A **B9 band smartwatch**: body 45.3 × 20 × 4.1 mm, 18 mm strap, charging contact on the back.
- Its **right-angle magnetic charging cable**: round head Ø6.3 × 5.9 mm, cable Ø3.3 mm.

If you have a different watch, the included OpenSCAD file lets you enter your own measurements (see Customising below).

## Files

- `watch-charging-bridge.stl`: the full bridge, 130 × 28 × 43 mm.
- `watch-charging-bridge-test.stl`: the top of the bridge only, 54 × 26 × 14 mm. It's a quick print that lets you check the charger and watch fit before printing the whole thing.
- `watch-charging-bridge.scad`: the parametric source file.

## Print settings

- **Orientation:** as supplied, standing on its flat base.
- **Supports:** none.
- **Layer height:** 0.2 mm (0.12–0.16 mm brings out the stone detail more).
- **Walls:** 3 perimeters.
- **Infill:** 15%.
- **Material:** PLA is fine. A grey or stone-coloured filament looks best.

If your printer is new to you, print the test piece first. The charger pocket and cradle are tight fits, and printers vary by a few tenths of a millimetre.

## Assembly

1. Push the round head of the charging plug into the pocket at the top of the bridge, **metal circle facing up**, with the cable pointing toward the back.
2. Press the cable along the slot, through the gap in the back wall, and down the groove in the back face.
3. Plug the USB end in.
4. Lay the watch face-up in the cradle, with its charging end (the end opposite the CE mark on the back) over the plug. Let the strap hang down both slopes.

## Customising

Open `watch-charging-bridge.scad` in [OpenSCAD](https://openscad.org). Every size is set at the top of the file:

- **Plug too tight or loose:** change `FIT` (default 0.3) by 0.1–0.2.
- **Watch tight in the cradle:** raise `IN_C` (default 10.3). Each 0.1 widens the cradle by 0.2 mm.
- **Watch not charging:** raise `PROUD` (default 0.24) to lift the contact slightly.
- **Different watch:** enter its length, width, thickness, curve depth and contact position. The crown curve, cradle and charger position all update to match.
- **Smooth finish:** set `stone_texture = false`.

Set `part = "test"` to export the test piece.
