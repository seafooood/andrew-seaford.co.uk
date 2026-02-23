---
keywords: [vs code, new tab, preview mode, settings, editor configuration]
---

# How To Force VS Code To Open Files In A New Tab

To force VS Code to open every file in a new tab (instead of reusing the same preview tab), you need to disable preview mode. Here’s how:

## Step 1 - Open Command Palette

- Open Command Palette: `Ctrl+Shift+P`

## Step 2 - Open Settings

- Type and select: `Preferences: Open Settings (UI)`

![alt text](image-1.png)

## Step 3 - enablePreview

- Search for: workbench.editor.enablePreview

- Uncheck setting `Workbench › Editor: Enable Preview`

![alt text](image-2.png)

- This ensures every file opens in a dedicated tab instead of reusing a single preview tab.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/vs-code/how-to-force-vs-code-to-open-files-in-a-new-tab](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/vs-code/how-to-force-vs-code-to-open-files-in-a-new-tab)

## VS Code Related Articles

- [VS Code Extension - Project Identity](../../../portfolio/vs-extension-project-identity/index.md)
- [How To Open Folder In VS Code](../open-folder-in-vs-code/index.md)

## Ubuntu Related Articles

- [How To Assign A Static Ip Address in Ubuntu](../../ubuntu/how-to-assign-a-static-ip-address-in-ubuntu/index.md)
- [How To Change Hostname In Ubuntu](../../ubuntu/how-to-change-hostname-in-ubuntu/index.md)
- [How to Customize Your Bash Prompt on Ubuntu](../../ubuntu/how-to-customize-your-bash-prompt-on-ubuntu/index.md)
