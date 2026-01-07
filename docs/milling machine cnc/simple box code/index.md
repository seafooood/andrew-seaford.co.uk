---
title: "Simple Box G Code"
date: 2019-01-23
categories: 
  - "cnc-mill"
tags: 
  - "cnc"
  - "gcode"
  - "marlin"
  - "milling"
slug: "simple-box-code"
---

**Goal** The goal of this procedure is to draw a simple box 10x10mm.

**Relevant** Marlin 3D Printer Firmware running on Arduino Mega with RAMPS 1.4 shield. Controlled via Pronterface.

**Procedure** The procedure below is a simple gcode example that will show how to draw a simple 10mm box.

1. Create a text file with the following code. In this example, we will call the text file box10x10mm.g  

```gcode
G91 
G1 X10 
G1 Y10 
G1 X-10 
G1 Y-10
```

2. Open Pronterface

3. Click the Connect button, to connect to the device.  

[![](images/buttonconnect-300x59.png)](images/buttonconnect.png)

4. Click the Home button, to home all of the axis.  

[![](images/buttonhome-300x262.png)](images/buttonhome.png)

5. Click the Load File button.

[![](images/buttonloadfile-300x60.png)](images/buttonloadfile.png)

6. Select the file created in step 1.

[![](images/step2-select-file-300x213.png)](images/step2-select-file.png)

7. Click the Print button.

[![](images/print-300x60.png)](images/print.png)
