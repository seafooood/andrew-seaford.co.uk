---
title: "Create empty folders using Inno"
keywords: [inno setup, create directories, dirs section, installer script]
date: 2015-02-23
categories:
  - "inno"
---

When installing a program using Inno, to create an empty directory you will need to add a dirs section to the installer script.

`[Dirs] Name: "{app}\Example1"`

Download installer script [CCreateEmptyDirectories.iss](createemptydirectories.iss)


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/create-empty-folders-inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/create-empty-folders-inno)

## Inno Setup Related Articles

- [Automatically Get Target Exe Version in Inno](../automatically-target-exe-version-inno/index.md)
- [Check DotNet Framework is installed during Inno Setup](../check-dotnet-framework-installed-inno-setup/index.md)
- [Check if a program exists before installing with Inno](../check-program-exists-installing-inno/index.md)
- [Customize Inno Setup Installer Images: WizardImageFile Guide](../custom-inno-theme/index.md)
- [Free Disk Space Inno](../free-disk-space-inno/index.md)
