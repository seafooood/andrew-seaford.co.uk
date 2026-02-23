---
title: "Reporting endstop status"
keywords: [cnc milling, endstop status, marlin firmware, troubleshooting, limit switches]
date: 2019-01-23
categories:
  - "cnc-mill"
tags:
  - "cnc"
  - "endstop"
  - "marlin"
  - "marlinfw"
  - "trigger"
---

## Symptoms

CNC machine reports incorrect end stop trigger.

## Relevant

Marlin 3D Printer Firmware running on Arduino Mega with RAMPS 1.4 shield. Controlled via Pronterface.

## Procedure

The status of the end switches can be checked using the command `M119`. The procedure below explains how to check the status of the switches.

### Step 1

- Click the Connect button  

![buttonconnect-300x59.png](images/buttonconnect-300x59.png)

## Step 2 

- Enter the command `M119` and then click the Send button. The command will display the status of each of the end switches.

![commandm119.png](images/commandm119.png)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/milling-machine-cnc/reporting-endstop-status](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/milling-machine-cnc/reporting-endstop-status)

## CNC Related Articles

- [Z Axis drops after completing job](../axis-drops-completing-job/index.md)
- [Marlinfw Homing Direction](../marlinfw-homing-direction/index.md)
- [Simple Box G Code](../simple-box-code/index.md)
- [3D Printed Puzzle Vase for Flowers — Ideal for Lego, Crochet, and Artificial Flower Displays](../../freecad/3d-printed-puzzle-vase-for-flowers/index.md)
- [3D Printed Toothbrush Holder](../../freecad/3d-printed-toothbrush-holder/index.md)
