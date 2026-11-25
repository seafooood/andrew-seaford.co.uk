---
title: "Tree Trunk Shelf Clamp"
keywords: [3d printing, shelf bracket, tree trunk clamp, christmas tree, openscad, stl model]
date: 2026-11-25
categories:
  - "3d-printing"
---

# Tree Trunk Shelf Clamp

A two-piece clamp that grips a tree trunk (or any round post) and holds a wooden shelf on top. Both halves are the same part, so you print one file twice.

It takes its idea from the centre clamp of a Christmas-tree train set. Wing bolts grip the trunk, and three L-bracket tabs on each half screw to the underside of the shelf.

## Features

- Two identical halves, so you only need one STL
- Prints upside down with no supports. The shelf face and the screw tabs sit flat on the bed.
- Captive M6 nuts in hex pockets, with the hex point up so the roof bridges cleanly
- Two wing bolts per half to grip the trunk and centre the clamp
- Six screw tabs with 45° gussets for a firm fixing to the shelf
- Parametric OpenSCAD source included, so you can change the bore, height and hole sizes

## Sizes

| | |
|---|---|
| Bore (inside diameter) | 80 mm |
| Outside diameter (ring) | 100 mm |
| Height | 30 mm |
| Wall | 10 mm |

For a different trunk size, open `tree_shelf_clamp.scad` and change `ri` (inner radius) and `ro` (outer radius). Keep the wall at about 10 mm.

## Hardware (one complete clamp)

- 4 × M6 hex nuts (pressed into the inner pockets)
- 4 × M6 bolts, 40–50 mm, with wing nuts (to grip the trunk; length depends on your trunk)
- 2 × M6 bolts, about 20 mm, with nuts (to join the two halves)
- 6 × wood screws, up to 4 mm diameter (to fix the tabs to the shelf)

## Print settings

- **Copies:** 2
- **Orientation:** as supplied (flat face down)
- **Supports:** none
- **Material:** PETG or ASA recommended. PLA works, but it can creep under a constant load in a warm room.
- **Walls:** 4 or more
- **Infill:** 30–40%
- **Layer height:** 0.2 mm

## Assembly

1. Press or glue an M6 nut into each hex pocket on the inner face.
2. Screw the wing bolts in from the outside until they just stand clear of the bore.
3. Put the two halves around the trunk with the flanges face to face.
4. Bolt the flanges together with the two short M6 bolts.
5. Slide the clamp to the height you want, with the flat tab face upwards.
6. Tighten the wing bolts evenly until the clamp grips the trunk and sits level.
7. Tighten the wing nuts against the clamp to lock the bolts.
8. Put the shelf on top and screw up through the six tabs into the shelf.

## Files

- `tree_shelf_clamp_half.stl` – print this twice
- `tree_shelf_clamp.scad` – parametric OpenSCAD source
