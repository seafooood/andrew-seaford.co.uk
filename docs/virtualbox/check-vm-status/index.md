# How to Automatically Check and Restart a VirtualBox VM on Ubuntu

## Introduction

Have you ever had a critical service running inside a VirtualBox virtual machine (VM), like a web server, database, or development environment, that needs to be online 24/7? If so, you might have worried about what would happen if the VM shuts down unexpectedly due to a server reboot or an error.

This guide is here to help you solve that exact problem. We'll walk you through creating a simple automated solution on **Ubuntu** that regularly checks if your VirtualBox VM is running and, if it's not, automatically starts it back up. By the end of this tutorial, you'll have a reliable setup that ensures your VM is always available when you need it.

## The Scripts

We'll use two simple shell scripts to accomplish this: one to check the VM status and another to set up a scheduled task.

### 1. The Status Checker Script (`check_vm_status.sh`)

This script checks if your specified VM is running. If it finds that the VM is not running, it will start it. It also keeps a log file so you can see when it has been run and what it did.

Here is the code. You will need to change the `VM_NAME` variable to the name of your virtual machine.

```bash
#!/bin/bash

# VM name
VM_NAME="docker-host-1"

# Log file
LOG_FILE="vm_check.log"

# Timestamp
TIMESTAMP=$(date)

# Check if the VM is running
if VBoxManage showvminfo "$VM_NAME" | grep -q "running (since"; then
    echo "--------------------------------" >> "$LOG_FILE"
    echo "Running check at $TIMESTAMP" >> "$LOG_FILE"
    echo "VM is already running." >> "$LOG_FILE"
else
    echo "--------------------------------" >> "$LOG_FILE"
    echo "Running check at $TIMESTAMP" >> "$LOG_FILE"
    echo "VM is not running. Starting it now..." >> "$LOG_FILE"
    VBoxManage startvm "$VM_NAME" --type headless >> "$LOG_FILE" 2>&1
    echo "VM started." >> "$LOG_FILE"
fi
```

### 2. The Cron Setup Script (`setup_cron.sh`)

This script creates a "cron job," which is a scheduled task that runs automatically at a specified time. This cron job will execute our `check_vm_status.sh` script every day at 4:00 AM.

**Important:** You will need to edit this script to provide the correct path to your `check_vm_status.sh` script.

```bash
#!/bin/bash

CRON_JOB="0 4 * * * /path/to/your/check_vm_status.sh"

# Add the cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job added successfully:"
echo "$CRON_JOB"
```

## Setup Instructions

Now, let's put it all together.

### Step 1: Save the Scripts

Save the two scripts above as `check_vm_status.sh` and `setup_cron.sh` in a directory of your choice on your Ubuntu machine.

### Step 2: Make the Scripts Executable

Open a terminal and navigate to the directory where you saved the files. Run the following command to make the scripts executable:

```bash
chmod +x check_vm_status.sh
chmod +x setup_cron.sh
```

### Step 3: Update the Path in `setup_cron.sh`

Before you run the setup script, you need to edit it to include the correct path to `check_vm_status.sh`.

1.  Get the full path to your script by running the following command in the directory where you saved the files:
    ```bash
    readlink -f check_vm_status.sh
    ```
2.  Copy the output of that command.
3.  Open `setup_cron.sh` in a text editor and paste the copied path in place of `/path/to/your/check_vm_status.sh`.

### Step 4: Run the Cron Setup Script

Now you are ready to set up the cron job. Run the following command:

```bash
./setup_cron.sh
```

You should see a confirmation message that the cron job was added successfully.

## Verifying the Setup

### Checking the Cron Job

You can verify that the cron job was added by running the following command:

```bash
crontab -l
```

This will list all the active cron jobs for the current user. You should see the line that was added by the setup script.

### Checking the Log File

The `check_vm_status.sh` script will create a `vm_check.log` file in the same directory. You can check this file to see the script's activity.

```bash
cat vm_check.log
```

You should see output similar to this:

```log
--------------------------------
Running check at Tue  4 Nov 21:13:19 GMT 2025
VM is already running.
```

## Conclusion

Congratulations! You now have an automated system that ensures your VirtualBox VM is always running. This simple solution provides peace of mind, knowing that your important services will automatically restart if they ever go down.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/check-vm-status](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/virtualbox/check-vm-status)
