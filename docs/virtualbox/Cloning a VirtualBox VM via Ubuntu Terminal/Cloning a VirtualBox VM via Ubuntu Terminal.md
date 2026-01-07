# Cloning a VirtualBox VM via Ubuntu Terminal  

## Introduction  

This guide explains how to clone a VirtualBox VM named **"Template Ubuntu Server 22.04"** to create a new VM called **"Langflow3"** on an **Ubuntu 22.04** host.  

## Steps  

### 1. Connect to the Host Server  

Use SSH or PuTTY to connect:  

```bash
ssh username@serverip
```  

### 2. List Available VMs  

Find the name of the VM to clone:  

```bash
vboxmanage list vms
```  

### 3. Clone the VM  

Clone **"Template Ubuntu Server 22.04"** to **"Langflow3"** and register it:  

```bash
VBoxManage clonevm "Template Ubuntu Server 22.04" --name "Langflow3" --register
```  

### 4. (Optional) Bridge Network  

Bridge the VM to the local network for easier access:  

```bash
vboxmanage modifyvm "Langflow3" --nic1 bridged --bridgeadapter1 eno1
```  

### 5. Start the VM  

Boot the VM in headless mode:  

```bash
vboxmanage startvm "Langflow3" --type headless
```  

### 6. (Optional) Find VM IP Address  

If Guest Additions is installed, retrieve the VM’s IP from the host:  

```bash
vboxmanage guestproperty get "Langflow3" "/VirtualBox/GuestInfo/Net/0/V4/IP"
```  

### 7. (Optional) Enable VNC Access  

Set up VNC for remote access (password limited to 8 characters):  

```bash
VBoxManage modifyvm "Langflow3" --vrdeport 3352
VBoxManage modifyvm "Langflow3" --vrdeproperty VNCPassword=Password1
```  

Connect via VNC using the **host IP**, **port 3352**, and **password "Password1"**.  

### 8. Take a Snapshot  

Create a snapshot to restore the VM to this state if needed:  

```bash
VBoxManage snapshot "Langflow3" take "Initial Working State" --live
```  

### 9. Power Down the VM

Shut down the VM gracefully:

```bash
vboxmanage controlvm "Langflow3" acpipowerbutton
```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Cloning%20a%20VirtualBox%20VM%20via%20Ubuntu%20Terminal](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/Cloning%20a%20VirtualBox%20VM%20via%20Ubuntu%20Terminal)
