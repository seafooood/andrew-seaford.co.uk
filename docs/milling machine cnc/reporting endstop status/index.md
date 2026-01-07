---
title: "Reporting endstop status"
date: 2019-01-23
categories: 
  - "cnc-mill"
tags: 
  - "cnc"
  - "endstop"
  - "marlin"
  - "marlinfw"
  - "trigger"
slug: "reporting-endstop-status"
---

**Symptoms** CNC machine reports incorrect end stop trigger.

**Relevant** Marlin 3D Printer Firmware running on Arduino Mega with RAMPS 1.4 shield. Controlled via Pronterface.

**Procedure** The status of the end switches can be checked using the command `M119`. The procedure below explains how to check the status of the switches.

1. Click the Connect button  
    [![](images/buttonconnect-300x59.png)](images/buttonconnect.png)  
      
      
    
2. Enter the command `M119` and then click the Send button. The command will display the status of each of the end switches.  
    [![](images/commandm119.png)](images/commandm119.png)
