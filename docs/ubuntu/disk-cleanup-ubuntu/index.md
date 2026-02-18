---
keywords: [ubuntu, disk cleanup, free space, apt autoremove, system maintenance]
---

# Disk Cleanup Ubuntu

## Introduction

This guide explains some safe steps to clean up the hard drive on an Ubuntu computer..

## Measure Disk Space

- To check the available space, execute the command `df`.

```bash
df
```

In this example, the root partition (/dev/mapper/ubuntu--vg-ubuntu--lv) mounted at `/` is completely full (100% used).

```log
harry@templateunbutu:/var/log$ df
Filesystem                        1K-blocks    Used Available Use% Mounted on
tmpfs                                812876    1076    811800   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   8408452 8273228         0 100% /
tmpfs                               4064380       0   4064380   0% /dev/shm
tmpfs                                  5120       0      5120   0% /run/lock
/dev/sda2                           1768056  268396   1391528  17% /boot
tmpfs                                812876       4    812872   1% /run/user/1000
```

## Steps

### Step 1. - Remove apt cache

- Remove old cached package downloads.

```bash
sudo apt clean
```

### Step 2. - Remove orphaned/unused packages

- Autoremove gets rid of packages no longer needed.

```bash
sudo apt autoremove --purge
```

### Step 3. - Clear old log files

- Ubuntu logs are stored in `/var/log`. Rotate logs older than 3 days and then clear the logs.

```bash
sudo journalctl --vacuum-time=3d
```

- That keeps only the last 3 days of system logs.
- Remove archived logs in `/var/log`.

```bash
sudo rm -f /var/log/*.gz
sudo rm -f /var/log/*.1
sudo rm -rf /var/log/journal/*
```

## Step 4. - Clear .cache Folder

- Clear the entire `.cache` folder. This is mostly rebuildable stuff like thumbnails, temp downloads, etc.

```bash
rm -rf ~/.cache/*
```

### 5. - Snap Cache

- Snap can grow silently. You can clean it up like this.

```bash
sudo du -sh /var/lib/snapd/cache
```

### Step 6. - Check for large files

- Check what’s eating up space:

```bash
sudo du -ahx / | sort -rh | head -n 20
```

## Summary

- Confirm that the clean up has been successful by issuing the `df` command.

- In this example, we can see that the root partition (/dev/mapper/ubuntu--vg-ubuntu--lv), mount at `/` used space has decreased from 100% to 80%.

```log
harry@templateunbutu:/var/log$ df
Filesystem                        1K-blocks    Used Available Use% Mounted on
tmpfs                                812876    1096    811780   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   8408452 6331344   1628392  80% /
tmpfs                               4064380       0   4064380   0% /dev/shm
tmpfs                                  5120       0      5120   0% /run/lock
/dev/sda2                           1768056  250660   1409264  16% /boot
tmpfs                                812876       4    812872   1% /run/user/1000
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/disk-cleanup-ubuntu](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/disk-cleanup-ubuntu)
