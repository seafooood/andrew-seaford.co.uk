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

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Installing%20VirtualBox%20Guest%20Additions%20in%20Ubuntu%20Guest%20Virtual%20Machine](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Installing%20VirtualBox%20Guest%20Additions%20in%20Ubuntu%20Guest%20Virtual%20Machine)
