---
title: "Free Disk Space Inno"
date: 2015-02-23
categories: 
  - "inno"
slug: "free-disk-space-inno"
---

To show a label on the Inno wizard page displaying the amount of require disk space. Add the following code section to the installer script. `[Code] procedure InitializeWizard; begin WizardForm.DiskSpaceLabel.Visible := True; // False to hide end;`

Download installer script [**FreeDiskSpace.iss**](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/FreeDiskSpace.iss "FreeDiskSpace.iss")


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/free%20disk%20space%20inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/free%20disk%20space%20inno)
