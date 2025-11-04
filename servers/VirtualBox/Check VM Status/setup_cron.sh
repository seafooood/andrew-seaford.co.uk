#!/bin/bash

CRON_JOB="0 4 * * * /home/andrew/Documents/network/check_vm_status.sh"

# Add the cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job added successfully:"
echo "$CRON_JOB"
