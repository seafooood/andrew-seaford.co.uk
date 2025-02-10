#!/bin/bash

# Directory to save exported VMs
EXPORT_DIR="/mnt/garry/20241211"

# Ensure the export directory exists
mkdir -p "$EXPORT_DIR"

# Get the list of all VMs
VMS=$(VBoxManage list vms | awk -F '"' '{print $2}')

# Check if any VMs are found
if [ -z "$VMS" ]; then
    echo "No VMs found in VirtualBox. Exiting."
    exit 1
fi

# Loop through each VM and export it
while IFS= read -r VM; do
    echo "Starting export for VM: $VM"

    # Create the export filename
    EXPORT_FILE="$EXPORT_DIR/$(echo "$VM" | tr ' ' '_').ova"

    # Try to export the VM
    if VBoxManage export "$VM" --output "$EXPORT_FILE"; then
        echo "Successfully exported $VM to $EXPORT_FILE"
    else
        echo "Failed to export $VM. Skipping to the next VM."
    fi

done <<< "$VMS"

echo "Export process completed."
