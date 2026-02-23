---
title: "Check if a program exists before installing with Inno"
keywords: [inno setup, file exists check, installer validation, pascal script]
date: 2015-02-23
categories:
  - "inno"
---

To check if a program exists before installing with Inno add the following code section to the installer script. In this example we will be testing for the file "c:\\Example\\Test.exe". If the test.exe file exist a message box showing "Program Already Exists" will be displayed and the installer will terminate.

`[Code] function IsMyProgramInstalled: boolean; begin result := FileExists('C:\Example\Test.exe'); end;  function InitializeSetup: boolean; begin result := not IsMyProgramInstalled; if not result then MsgBox('Program Already Exists', mbError, MB_OK); end;`

Download the installer script [**IsMyProgramInstalled.iss**](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ismyprograminstalled.iss "IsMyProgramInstalled.iss")


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/check-program-exists-installing-inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/check-program-exists-installing-inno)

## Inno Setup Related Articles

- [Automatically Get Target Exe Version in Inno](../automatically-target-exe-version-inno/index.md)
- [Check DotNet Framework is installed during Inno Setup](../check-dotnet-framework-installed-inno-setup/index.md)
- [Create empty folders using Inno](../create-empty-folders-inno/index.md)
- [Customize Inno Setup Installer Images: WizardImageFile Guide](../custom-inno-theme/index.md)
- [Free Disk Space Inno](../free-disk-space-inno/index.md)
