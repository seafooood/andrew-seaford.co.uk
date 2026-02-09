# Force Stopping VirtualBox VM

## Problem Description

When a VirtualBox VM gets stuck in the "stopping" state and doesn't respond to normal shutdown commands, you may need to force stop it. This can happen when:

- The VM becomes unresponsive
- Host system runs out of memory
- VNC connections fail
- Normal shutdown commands timeout

## Prerequisites

- Root/sudo access to the Ubuntu host server
- SSH access to the VirtualBox host
- VM is stuck in "stopping" or similar unresponsive state

## Step-by-Step Procedure

### Step 1. Identify the Problem VM

First, list all VMs to find the problematic one:

```bash
VBoxManage list vms
```

### Step 2. Check VM State

Verify the current state of the stuck VM:

```bash
VBoxManage showvminfo "VM_NAME" | grep "State"
```

*Example output: `State: stopping (since 2026-02-09T11:09:02.590000000)`*

### Step 3. Check Running VMs

Confirm which VMs are actually running:

```bash
VBoxManage list runningvms
```

### step 4. Attempt Normal Force Stop (Optional)

Try the normal force stop command first:
```bash
VBoxManage controlvm "VM_NAME" poweroff
```

*This may fail with error: "The virtual machine is being powered down"*

### Step 5. Find and Kill the VBoxHeadless Process

If normal force stop fails, identify the stuck process:
```bash
ps aux | grep -i "VM_NAME"
```

*Look for VBoxHeadless processes with high CPU/memory usage*

### Step 6. Force Kill the Process

Kill the stuck VBoxHeadless process:
```bash
sudo kill -9 [PID]
```
*Replace [PID] with the actual process ID from step 5*

### Step 7. Verify Process Termination

Confirm the process is gone:
```bash
ps aux | grep -i "VM_NAME"
```

*Should only show the grep command itself*

### Step 8. Check VM State

Verify the VM state has changed:

```bash
VBoxManage showvminfo "VM_NAME" | grep "State"
```
*State should change to "aborted" or "powered off"*

### Step 9. Restart VM (When Ready)

Once the VM is properly stopped, you can start it again:
```bash
VBoxManage startvm "VM_NAME" --type headless
```

## Important Notes

**Data Loss Warning**: Force killing a VM will result in loss of any unsaved data in RAM. Only use this method when:

- The VM is completely unresponsive
- Normal shutdown methods have failed
- You're prepared to lose current memory state

**Memory Management**: If the host was running low on memory (97%+ usage), consider:

- Stopping other non-essential VMs first
- Monitoring host memory usage before restarting
- Adjusting VM memory allocations if needed

## Troubleshooting Tips

- If `kill -9` doesn't work immediately, wait a few seconds and check again
- Multiple VBoxHeadless processes might exist for the same VM - kill all of them
- After force stopping, always verify the VM state before attempting to restart
- Consider checking VirtualBox logs if problems persist: `/var/log/vbox/`
