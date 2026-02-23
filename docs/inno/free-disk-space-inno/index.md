---
title: "Free Disk Space Inno"
keywords: [inno setup, disk space label, wizard page, installer script]
date: 2015-02-23
categories:
  - "inno"
---

To show a label on the Inno wizard page displaying the amount of require disk space. Add the following code section to the installer script. `[Code] procedure InitializeWizard; begin WizardForm.DiskSpaceLabel.Visible := True; // False to hide end;`

Download installer script [**FreeDiskSpace.iss**](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/freediskspace.iss "FreeDiskSpace.iss")


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/free-disk-space-inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/free-disk-space-inno)

## Inno Setup Related Articles

- [Automatically Get Target Exe Version in Inno](../automatically-target-exe-version-inno/index.md)
- [Check DotNet Framework is installed during Inno Setup](../check-dotnet-framework-installed-inno-setup/index.md)
- [Check if a program exists before installing with Inno](../check-program-exists-installing-inno/index.md)
- [Create empty folders using Inno](../create-empty-folders-inno/index.md)
- [Customize Inno Setup Installer Images: WizardImageFile Guide](../custom-inno-theme/index.md)
