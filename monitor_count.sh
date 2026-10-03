#!/bin/bash


timestamp=$(date +"%Y%m%d_%H%M%S")

monitor_counts="output/monitor_counts_${timestamp}.txt"

tail -n +2 data/bp_readings.csv \
  | cut -d ',' -f2 \
  | sort \
  |uniq -c > "$monitor_counts"