# How To Open Folder In VS Code

## Introduction

After moving to Ubuntu one of the feature that I missed from Windows OS, we the ability to right click in a folder and open the folder in VS Code. This article explains how to configure the feature in Nautilus, often called *Files* in the GNOME desktop environment (which Ubuntu uses by default).

## Procedure

### Step 1 - Create Script Folder

Create the scripts directory if it doesn't exist.

```bash
mkdir -p ~/.local/share/nautilus/scripts
```

### Step 2 - Create Script File

```bash
nano ~/.local/share/nautilus/scripts/Open\ in\ VS\ Code
```

### Step 3 - Paste Code

Paste in this code

```bash
#!/bin/bash
selected=$(echo "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS" | head -1 | tr -d '\n')
code "$selected"
```

### Step 4 - Change Permission

Make the file executable

```bash
chmod +x ~/.local/share/nautilus/scripts/Open\ in\ VS\ Code
```

### Step 5 - Restart Nautilus

```bash
nautilus -q
```

## Summary

Now when you right click on a folder (on a folder, not in a folder), you will see **Scripts > Open in VS Code**

## Ubuntu Related Articles

- [How To Force VS Code To Open Files In A New Tab](../how-to-force-vs-code-to-open-files-in-a-new-tab/index.md)
- [VS Code Extension - Project Identity](../../../portfolio/vs-extension-project-identity/index.md)