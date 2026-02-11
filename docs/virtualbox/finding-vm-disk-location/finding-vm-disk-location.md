# Finding VM Disk Location

## Introduction

In this article we will find the location of a Virtual Box VM called `n8nsept25`.

## Procedure

### Step 1. Locate your VM folder Run this command to find exactly where the files are stored:

```bash
vboxmanage showvminfo "n8nsept25" | grep "Config file"
```

This will show you a path like `/home/user/VirtualBox VMs/n8nsept25/n8nsept25.vbox`.

### Step 2. Copy the entire directory Use the cp command to copy the entire folder to your backup location.

    Note: If your host machine is also low on space, ensure the destination (like an external drive or a different partition) has enough room for the full size of the .vdi file.

Bash

# Example: Copying to a backup folder in your home directory
cp -R "/path/to/n8nsept25_folder" ~/vm_backup_n8nsept25

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Finding%20VM%20Disk%20Location](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Finding%20VM%20Disk%20Location)
