# How To Assign A Static Ip Address in Ubuntu

## Step 1. Identify Your Network Interface

First, open a terminal and run:

```bash
ip a
```

Look for an interface like `eth0`, `ens33`, `enp0s3`, or `wlan0` (for Wi-Fi).

## Step 2. Find Your Current Network Details

Run:

```bash
ip route
```

This will show the default gateway (usually something like `192.168.1.1` or `192.168.0.1`).

## Step 3. Edit Netplan Configuration

Ubuntu (18.04 and newer) uses Netplan for network configuration.

The filename may vary, so check with:

```bash
ls /etc/netplan/
```

Edit the Netplan file:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

## Step 4. Configure a Static IP

Modify the file to something like this:

```yaml
network:
  version: 2
  ethernets:
    eth0:  # Change this to your actual interface name
      dhcp4: no
      addresses:
        - 192.168.1.100/24  # Your desired static IP
      gateway4: 192.168.1.1  # Your router's IP (default gateway)
      nameservers:
        addresses:
          - 8.8.8.8  # Google DNS
          - 1.1.1.1  # Cloudflare DNS
```

Replace:

- `eth0` with your actual network interface.
- `192.168.1.100` with your preferred static IP.
- `192.168.1.1` with your router’s actual IP.

## Step 5. Apply the Changes

Run:

```bash
sudo netplan apply
```

## Step 6. Verify the Static IP

Run:

```bash
ip a
```

Check if your interface has the correct static IP.

You can also test connectivity:

```bash
ping 8.8.8.8
```
