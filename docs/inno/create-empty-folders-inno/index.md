---
title: "Create empty folders using Inno"
description: "How to create empty directories during installation with Inno Setup on Windows, with example [Dirs] entries, options explained, and expected output."
keywords: ["inno setup", "inno", "empty folders", "dirs", "installer"]
slug: "create-empty-folders-inno"
date: 2015-02-23
categories:
  - "inno"
---

When working with Inno Setup, you might need the installer to create empty folders on the user's machine. This commonly happens when your application expects certain directories to exist for logs, configuration, or runtime data even when they contain no files yet.

This guide will walk you through the simple `[Dirs]` entry to create empty directories during installation and explain the common options you may want to use. The examples assume you are building an installer for Windows using Inno Setup.

Example minimal entry to create a single empty folder under the application directory:

```
[Dirs]
Name: "{app}\Example1"
```

Download the example installer script: [CreateEmptyDirectories.iss](createemptydirectories.iss)


## Expected output

After running the installer with the `[Dirs]` entry above, the installer will:

- Create the folder `Example1` inside the chosen application installation folder (`{app}`) even if it contains no files.
- Ensure the folder exists for your application to write logs or create files at runtime.
- Optionally write entries to the installation log showing the created directory path.

If the target folder already exists, Inno Setup will leave it unchanged and continue the install without error.

## Related Files

- [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/create-empty-folders-inno](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/create-empty-folders-inno)

## Inno Setup Related Articles

- [Automatically Get Target Exe Version in Inno](../automatically-target-exe-version-inno/index.md)
- [Check DotNet Framework is installed during Inno Setup](../check-dotnet-framework-installed-inno-setup/index.md)
- [Check if a program exists before installing with Inno](../check-program-exists-installing-inno/index.md)
- [Customize Inno Setup Installer Images: WizardImageFile Guide](../custom-inno-theme/index.md)
- [Free Disk Space Inno](../free-disk-space-inno/index.md)
