---
keywords: [virtualbox, snapshot, VBoxManage, backup, ubuntu terminal]
---

# Taking a Virtual Machine Snapshot via Ubuntu Terminal

## Introduction

Creating a Virtual Machine Snapshot, is a little bit lite creating a restore point in Windows. The Snapshot records the current state of the virtual machine and allow you revert back to the stored state incase something goes wrong with the virtual machine.

You can take a snapshot from the host console using the following command:

## Steps

### Step 1. - Take Snapshot

```sh
VBoxManage snapshot "Langflow3" take "MySnapshotName" --live
```

- `"Langflow3"` → Your VM name.
- `"MySnapshotName"` → Replace with a meaningful name for the snapshot.
- `--live` → (Optional) This allows you to take a snapshot while the VM is running.

### Step 2. - Verify the snapshot

- To check if the snapshot was successfully created, run:

```sh
VBoxManage snapshot "Langflow3" list
```

### Step 3. - Restore a snapshot

- If you ever need to revert to a snapshot:

```sh
VBoxManage snapshot "Langflow3" restore "MySnapshotName"
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/taking-a-virtual-machine-snapshot-via-ubuntu-terminal](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/taking-a-virtual-machine-snapshot-via-ubuntu-terminal)

## VirtualBox Related Articles

- [Attaching a DVD ISO Image in VirtualBox](../attaching-a-dvd-iso-image-in-virtualbox/index.md)
- [How to Automatically Check and Restart a VirtualBox VM on Ubuntu](../check-vm-status/index.md)
- [Cloning a VirtualBox VM via Ubuntu Terminal](../cloning-a-virtualbox-vm-via-ubuntu-terminal/index.md)
- [Finding VM Disk Location](../finding-vm-disk-location/index.md)
- [Force Stopping VirtualBox VM](../force-stop-virtualbox-vm/index.md)
