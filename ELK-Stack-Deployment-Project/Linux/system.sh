#!/bin/bash

# Free memory output to a free_mem.txt file
echo -e "Memory Info: \n" > ~/backups/freemem/free_mem.txt
free -mh > ~/backups/freemem/free_mem.txt

# Disk usage output to a disk_usage.txt file
echo -e "Disk Usage: \n" > ~/backups/diskuse/disk_usage.txt
df -H | awk '{print $3,$2,$5}' > ~/backups/diskuse/disk_usage.txt

# List open files to a open_list.txt file
echo -e "Open file: \n" > ~/backups/openlist/open_list.txt
lsof > ~/backups/openlist/open_list.txt

# Free disk space to a free_disk.txt file
echo "Free Disk Space: \n" > ~/backups/freedisk/free_disk.txt
df -h > ~/backups/freedisk/free_disk.txt
