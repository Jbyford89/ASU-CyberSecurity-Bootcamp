#!/bin/bash

mkdir -p /var/backup

tar cvzWf /var/backup/home.tar.gz /home

# moving file to new directory
mv /var/backup/home.tar.gz /var/backup/home.06172022.tar.gz

# creating a current one as well as a dated one with moving the file above command
tar cvzWf /var/backup/home.tar.gz /home

# list all files in /var/backup
ls -lah /var/backup >> /var/backup/file_report.txt

# print free memory
free -h >>/var/backup/disk_report.txt
