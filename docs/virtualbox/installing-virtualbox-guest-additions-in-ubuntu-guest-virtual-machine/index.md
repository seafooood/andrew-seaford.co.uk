---
keywords: [virtualbox, guest additions, ubuntu, virtual machine, VNC]
---

# Installing VirtualBox Guest Additions in Ubuntu Guest Virtual Machine

## Introduction  

This guide explains how to installing VirtualBox Guest Additions in Ubuntu Guest Virtual Machine. Installing Guest Additions enable additional functionality such as the ability to get the guest ip address from the host sever.

## Steps

### Step 1 - Connect To The Guest VM

- Use VNC to connect to the guest vm.

### Step 2. - Install Guest Additions

- Inside the VM, execute the install command.

```bash
sudo apt update
sudo apt install virtualbox-guest-utils
```

### Step 3. - (Optional) Confirm Guest Additions Installation

- Confirm Guest Additions has been successfully installed by executing the command to get all of the Guest Additions Properties.

```bash
sudo VBoxControl guestproperty enumerate
```

### Step 4. - (Optional) Get Guest Additions Properties From Host

- Now that Guest Additions has been installed, you can request Guest Additions Properties From Host server. Such the ip address of the virtual machine.

- From the host server, execute the command to get the ip address. In this example, we are going to get the ip address from a virtual machine called "Langflow3".

```bash
VBoxManage guestproperty get "Langflow3" "/VirtualBox/GuestInfo/Net/1/V4/IP"
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/installing-virtualbox-guest-additions-in-ubuntu-guest-virtual-machine](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/installing-virtualbox-guest-additions-in-ubuntu-guest-virtual-machine)

## VirtualBox Related Articles

- [Attaching a DVD ISO Image in VirtualBox](../attaching-a-dvd-iso-image-in-virtualbox/index.md)
- [How to Automatically Check and Restart a VirtualBox VM on Ubuntu](../check-vm-status/index.md)
- [Cloning a VirtualBox VM via Ubuntu Terminal](../cloning-a-virtualbox-vm-via-ubuntu-terminal/index.md)
- [Finding VM Disk Location](../finding-vm-disk-location/index.md)
- [Force Stopping VirtualBox VM](../force-stop-virtualbox-vm/index.md)
