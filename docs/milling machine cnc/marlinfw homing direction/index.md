---
title: "Marlinfw Homing Direction"
date: 2019-01-23
categories: 
  - "cnc-mill"
tags: 
  - "cnc"
  - "marlin"
  - "marlinfw"
  - "milling"
slug: "marlinfw-homing-direction"
---

**Symptoms** CNC machine homes in the wrong direction.

**Relevant** Marlin 3D Printer Firmware running on Arduino Mega with RAMPS 1.4 shield.

**Procedure** The direction of travel when homing is configured in the configuration.h using the settings X\_HOME\_DIR, Y\_HOME\_DIR and Z\_HOME\_DIR in the section ENDSTOP SETTINGS. A value of -1 will set the homing direction towards the min end stop. A value of 1 will set the homing direction to the max end stop.

In the example below the homing direction for the z axis will be changed to home towards the max end stop.  
[![](images/homedirold-300x160.png)](images/homedirold.png)  
  
  
  
  
The Z home value was -1 and has been changed to 1. 
  
[![](images/homedirnew-300x160.png)](images/homedirnew.png)
