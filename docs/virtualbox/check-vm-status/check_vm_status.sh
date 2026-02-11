#!/bin/bash

VM_NAME="n8nsept25"
LOG_FILE="/home/andrew/Documents/network/vm_check.log"

echo "--------------------------------" >> $LOG_FILE
echo "Running check at $(date)" >> $LOG_FILE

# Check if the VM is running
if ! VBoxManage showvminfo "$VM_NAME" | grep -q "running (since"; then
    echo "VM is not running. Starting it now..." >> $LOG_FILE
    VBoxManage startvm "$VM_NAME" --type headless >> $LOG_FILE 2>&1
    if [ $? -eq 0 ]; then
        echo "VM started successfully." >> $LOG_FILE
    else
        echo "Failed to start VM." >> $LOG_FILE
    fi
else
    echo "VM is already running." >> $LOG_FILE
fi
