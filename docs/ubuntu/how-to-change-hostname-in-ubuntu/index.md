---
keywords: [ubuntu, hostname, hostnamectl, network configuration]
---

# How To Change Hostname In Ubuntu

To change the hostname in Ubuntu, follow these steps:

## Step 1. Check Current Hostname

Run:

```bash
hostnamectl
```

It will display the current hostname.

## Step 2. Update /etc/hosts

Edit the /etc/hosts file:

```bash
sudo nano /etc/hosts
```

Find the line with your old hostname (usually associated with 127.0.1.1) and replace it with the new hostname. It should look like:

```cpp
127.0.1.1    new-hostname
```

Save and exit (CTRL+X, then Y, then Enter).

## Step 3. Restart or Apply Changes

Either restart your system:

```bash
sudo reboot
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/how-to-change-hostname-in-ubuntu](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/how-to-change-hostname-in-ubuntu)

## Ubuntu Related Articles

- [Apt vs Apt-get Commands on Ubuntu](../apt-vs-apt-get/index.md)
- [Disk Cleanup Ubuntu](../disk-cleanup-ubuntu/index.md)
- [How To Assign A Static Ip Address in Ubuntu](../how-to-assign-a-static-ip-address-in-ubuntu/index.md)
- [How to Customize Your Bash Prompt on Ubuntu](../how-to-customize-your-bash-prompt-on-ubuntu/index.md)
- [Ubuntu 12.4 Enable SSH Service](../ubuntu-12-4-enable-ssh-service/index.md)
