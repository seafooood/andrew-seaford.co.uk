# How To Create Template Documents

## Introduction

After moving to Ubuntu one of the feature that I missed from Windows OS, we the ability to right click in any folder and create a new file. This article explains how to configure the feature in Nautilus, often called *Files* in the GNOME desktop environment (which Ubuntu uses by default).

## Procedure

Any file you put in your `~/Templates` folder will appear in the right-click "New Document" submenu in Nautilus.

### Step 1 - Create Template File

Open a terminal and run

```bash

touch ~/Templates/Markdown.md
```

### Step 2 - Test

Right-click in any folder in Files

**Files > New Document > Markdown.md**

That's it!. The "New Document" option appears in the context menu once the Templates folder has at least one file in it.

## Ubuntu Related Articles

- [Apt vs Apt-get Commands on Ubuntu](../apt-vs-apt-get/index.md)
- [Disk Cleanup Ubuntu](../disk-cleanup-ubuntu/index.md)
- [How To Assign A Static Ip Address in Ubuntu](../how-to-assign-a-static-ip-address-in-ubuntu/index.md)
- [How To Change Hostname In Ubuntu](../how-to-change-hostname-in-ubuntu/index.md)
- [How to Play a Sound When Claude Code Needs Your Attention](../../claude/claude-code-notification-sounds/claude-code-notification-sounds.md)