---
title: "Automatically Get Target Exe Version in Inno"
date: 2015-02-18
categories: 
  - "inno"
tags: 
  - "inno"
  - "installer"
  - "version-number"
---

This example shows how to automatically update the version numbers for you Inno installer based on the version number of the target exe program.

In this example the installer will be installing a program called notepad.exe.

At the top of the script. The version number from the target exe is stored in the variable MyAppVersion

`#define MyAppVersion GetFileVersion("notepad.exe")`

In the Setup section the MyAppVersion is used to set the installer version number, product version number and used as part of the installer name.

```yml
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion} 
OutputBaseFilename=Setup{#MyAppName}{#MyAppVersion} 
VersionInfoVersion={#MyAppVersion}
```

Download the full installer code [AutoGetVersionNumber.iss](autogetversionnumber.iss)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/automatically-target-exe-version-inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/automatically-target-exe-version-inno)
