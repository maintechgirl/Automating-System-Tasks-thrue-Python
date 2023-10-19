#!/bin/bash

for logfile in var/log/*log; do
    echo "Processing $logfile"
    cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
done