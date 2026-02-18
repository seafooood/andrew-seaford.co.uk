---
title: "Z Axis drops after completing job"
keywords: [cnc milling, z axis, marlin firmware, stepper motor, troubleshooting]
date: 2019-02-02
categories:
  - "cnc-mill"
---

**Symptoms** CNC machine Z Axis drops after completing job.

**Relevant** Marlin 3D Printer Firmware running on Arduino Mega with RAMPS 1.4 shield. Controlled via Pronterface.

**Procedure** The steppers motors will shut down DEFAULT\_STEPPER\_DEACTIVE\_TIME seconds after the last move when DISABLE\_INACTIVE\_? is true. Individual axis can be disabled or DEFAULT\_STEPPER\_DEACTIVE\_TIME can be set to zero to stop the axis from dropping.

1. Open the firmware project
2. Open file Configuration\_adv.h
3. Change the line from  
      
    #define DEFAULT\_STEPPER\_DEACTIVE\_TIME 120  
      
    to  
      
    #define DEFAULT\_STEPPER\_DEACTIVE\_TIME 0
4. Upload firmware project


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/milling-machine-cnc/axis-drops-completing-job](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/milling-machine-cnc/axis-drops-completing-job)
