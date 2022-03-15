#!/bin/bash

lynis audit --test-from-group malware,authentication,networking,storage,filesystems >> /tmp/lynis.partial_scan.log 


