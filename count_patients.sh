#!/bin/bash

record_count="output/record_count.txt"

echo "Encounter records: $(tail -n +2 data/bp_readings.csv | wc -l)" > "$record_count"

