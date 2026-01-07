# Attaching a DVD ISO Image in VirtualBox

When working with VirtualBox, you'll often need to attach a DVD ISO image to a virtual machine. This could be for installing an operating system, using a live CD for troubleshooting, or running software from a disk image.

This guide will walk you through how to attach a DVD ISO image in VirtualBox using both the graphical interface and the command line on a Linux system.

## Manual Process

1. Open VirtualBox.
2. Select your virtual machine and go to **Settings > Storage**.
3. In the "Storage Devices" section, click on the empty CD icon under your IDE or SATA controller.
4. In the "Attributes" panel on the right, click the CD icon and select **Choose a disk file...**.
5. Browse to your ISO file and select it.
6. Click **OK** to save the settings.

## Terminal Process

If you prefer working on the command line, you can use the `VBoxManage` tool to attach an ISO image.

### Step 1: View the storage controllers

First, you need to identify the storage controller and port to which you want to attach the ISO. You can do this by running the following command, replacing `"n8nsept25"` with the name of your virtual machine:

```bash
VBoxManage showvminfo "n8nsept25" | grep -A 10 "Storage Controllers:"
```

You'll see an output similar to this:

```log
$ VBoxManage showvminfo "n8nsept25" | grep -A 10 "Storage Controllers:"
Storage Controllers:
#0: 'IDE', Type: PIIX4, Instance: 0, Ports: 2 (max 2), Bootable
  Port 1, Unit 0: Empty, ejected
#1: 'SATA', Type: IntelAhci, Instance: 0, Ports: 1 (max 30), Bootable
  Port 0, Unit 0: UUID: de1e9a44-e260-4566-aa5c-d9c45650f426
    Location: "/home/vboxadmin/don/n8nsept25/Snapshots/{de1e9a44-e260-4566-aa5c-d9c45650f426}.vdi"
```

In this example, the log shows that device #0 on the 'IDE' controller is `Empty, ejected`. We can use this port.

### Step 2: Attach the ISO disk image

Now, attach the ISO image. You'll need the name of your VM, the storage controller (`IDE` in this case), the port (`1`), the device (`0`), and the path to your ISO file.

```bash
VBoxManage storageattach "n8nsept25" --storagectl "IDE" --port 1 --device 0 --type dvddrive --medium "/home/vboxadmin/don/iso/gparted-live-1.7.0-1-amd64.iso"
```

### Step 3: Confirm the image has been attached

You can verify that the ISO has been attached by running the `showvminfo` command again:

```bash
VBoxManage showvminfo "n8nsept25" | grep -A 10 "Storage Controllers:"
```

The output should now show the path to your ISO file:

```log
Storage Controllers:
#0: 'IDE', Type: PIIX4, Instance: 0, Ports: 2 (max 2), Bootable
  Port 1, Unit 0: UUID: e8e33bdc-b990-4f41-bf9d-276f1ce9edb9
    Location: "/home/vboxadmin/don/iso/gparted-live-1.7.0-1-amd64.iso"
```

### Step 4: Change the boot order

If you want to boot from the ISO image, you'll need to change the boot order of your virtual machine.

```bash
VBoxManage modifyvm "n8nsept25" --boot1 dvd
```

This command sets the primary boot device to the DVD drive.

### Step 5: Detach (eject) the disk image

Once you're finished with the ISO image, you can eject it using the following command:

```bash
VBoxManage storageattach "n8nsept25" --storagectl "IDE" --port 1 --device 0 --type dvddrive --medium emptydrive
```

## Conclusion

Whether you prefer a graphical interface or the command line, VirtualBox makes it easy to attach and manage DVD ISO images. By following the steps in this guide, you can quickly attach an ISO for OS installations, recovery tools, or any other purpose.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Attaching-a-DVD-ISO-Image-in-VirtualBox](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Attaching-a-DVD-ISO-Image-in-VirtualBox)
