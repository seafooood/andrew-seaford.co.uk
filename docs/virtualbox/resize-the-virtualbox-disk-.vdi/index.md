---
keywords: [virtualbox, resize disk, VDI, disk space, VBoxManage]
---

# Resize the VirtualBox Disk (.vdi)

## Introduction  

This guide explains how to extend the size of the guest VM hard disk in VirtualBox. In this example, we are going to extend the hard disk for a vm called `Langflow5`.

The vm is struggling because 97% of the root partition has been used.

```log
harry@templateunbutu:~$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              794M  1.1M  793M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  8.1G  7.4G  293M  97% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          1.7G  245M  1.4G  16% /boot
tmpfs                              794M  4.0K  794M   1% /run/user/1000
```

## Steps

### Step 1. Connect to the Host Server  

Use SSH or PuTTY to connect:  

```bash
ssh username@serverip
```

### Step 2. - Shutdown the VM

- Make sure the VM is completely powered off (not just saved or paused).

```bash
vboxmanage controlvm "Langflow5" acpipowerbutton
```

### Step 3. - Find path To The Hard Disk

- Find the path to your VM's virtual disk.

```bash
VBoxManage list hdds
```

- In this example, the UUID is `/home/vboxadmin/don/Langflow5/Langflow5.vdi`.

```log
UUID:           863a1d6d-71e5-4d72-9de4-e05393de0803
Parent UUID:    base
State:          locked write
Type:           normal (base)
Location:       /home/vboxadmin/don/Langflow5/Langflow5.vdi
Storage format: VDI
Capacity:       10240 MBytes
Encryption:     disabled
```

### Step 4. - Increase size

- Resize the disk (example: increase to 50 GB).

```bash
VBoxManage modifyhd /home/vboxadmin/don/Langflow5/Langflow5.vdi --resize 51200
```

### Step 5. - Start the VM  

Boot the VM in headless mode:  

```bash
vboxmanage startvm "Langflow5" --type headless
```  

### Step 6. - Grow The Guest Partition

1. Download GParted Live ISO
Get it here:
👉 https://gparted.org/livecd.php

2. Attach the ISO in VirtualBox
Open VirtualBox

Select your VM → Settings → Storage

Click the CD icon next to the optical drive

Choose the GParted ISO

3. Boot the VM into GParted
Start the VM

You should boot into the GParted environment

If prompted, just go with the default options

4. Resize /dev/sda3
In the GParted UI:

Select the sda3 partition

Right-click → Resize/Move

Drag the slider all the way to the right (or type in full size, e.g., ~48GB)

Click Apply

This operation will resize the physical partition (/dev/sda3) without touching your data

5. Shutdown GParted & Boot Back to Ubuntu
Power off the VM

In VirtualBox, remove the GParted ISO from the CD drive (Settings → Storage)

Boot your VM as usual

### Step 7. Grow

- Once you're back in guest:

```bash
sudo pvresize /dev/sda3
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```

### Step 8. - Confirm Hard Drive has been extended

- Finally:

```bash
df -h
```

- You should see something like 48G total on / 

```log
harry@templateunbutu:~$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              794M  1.1M  793M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   48G  7.4G   39G  17% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          1.7G  245M  1.4G  16% /boot
tmpfs                              794M  4.0K  794M   1% /run/user/1000
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/resize-the-virtualbox-disk-.vdi)](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/resize-the-virtualbox-disk-.vdi))
