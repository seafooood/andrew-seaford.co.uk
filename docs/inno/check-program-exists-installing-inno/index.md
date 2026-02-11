---
title: "Check if a program exists before installing with Inno"
date: 2015-02-23
categories: 
  - "inno"
slug: "check-program-exists-installing-inno"
---

To check if a program exists before installing with Inno add the following code section to the installer script. In this example we will be testing for the file "c:\\Example\\Test.exe". If the test.exe file exist a message box showing "Program Already Exists" will be displayed and the installer will terminate.

`[Code] function IsMyProgramInstalled: boolean; begin result := FileExists('C:\Example\Test.exe'); end;  function InitializeSetup: boolean; begin result := not IsMyProgramInstalled; if not result then MsgBox('Program Already Exists', mbError, MB_OK); end;`

Download the installer script [**IsMyProgramInstalled.iss**](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/IsMyProgramInstalled.iss "IsMyProgramInstalled.iss")


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/check%20program%20exists%20installing%20inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/check%20program%20exists%20installing%20inno)
