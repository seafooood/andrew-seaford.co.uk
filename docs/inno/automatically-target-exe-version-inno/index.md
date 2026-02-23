---
title: "Automatically Get Target Exe Version in Inno"
keywords: [inno setup, version number, exe version, installer script, automation]
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

## Inno Setup Related Articles

- [Check DotNet Framework is installed during Inno Setup](../check-dotnet-framework-installed-inno-setup/index.md)
- [Check if a program exists before installing with Inno](../check-program-exists-installing-inno/index.md)
- [Create empty folders using Inno](../create-empty-folders-inno/index.md)
- [Customize Inno Setup Installer Images: WizardImageFile Guide](../custom-inno-theme/index.md)
- [Free Disk Space Inno](../free-disk-space-inno/index.md)
