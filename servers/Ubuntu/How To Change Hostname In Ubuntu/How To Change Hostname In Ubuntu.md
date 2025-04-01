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
