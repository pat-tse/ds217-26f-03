"""Assignment 03: summarize a telemetry ward's systolic readings.

Run from the assignment directory with the project environment active:

    python3 analysis.py
"""

from statistics import mean
import numpy as np


def load_readings(filename):
    """Return (patient_ids, monitors, hour_columns, readings) from the supplied CSV.

    readings is a 2D array of integers: one row per patient, one column per
    monitored hour, in the order the header lists them.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    header = lines[0].strip().split(",")
    rows = [line.strip().split(",") for line in lines[1:] if line.strip()]

    patient_ids = np.array([row[0] for row in rows])
    monitors = np.array([row[1] for row in rows])
    hour_columns = np.array(header[2:])
    readings = np.array([row[2:] for row in rows]).astype(int)
    return patient_ids, monitors, hour_columns, readings


def main():
    patient_ids, monitors, hour_columns, readings = load_readings("data/bp_readings.csv")
    print(f"Loaded {readings.shape[0]} patients x {readings.shape[1]} hours")
    # TODO: answer each question in the README's summary table with NumPy.
    patients = str(np.size(patient_ids))
    total_readings = str(np.size(readings))
    mean_sbp = str(np.mean(readings))
    sd_sbp = str(np.std(readings))
    min_sbp = str(np.min(readings))
    max_sbp = str(np.max(readings))
    stage2_patients = str(np.sum(np.mean(readings, axis=1) >= 140))
    highest_patient = str(patient_ids[np.argmax(np.mean(readings, axis = 1))])
    highest_patient_mean = str(np.max(np.mean(readings, axis=1)))
    peak_hour_column = str(hour_columns[np.argmax(np.mean(readings, axis = 0))])
    peak_hour_mean = str(np.max(np.mean(readings, axis = 0)))

    unique_monitors = sorted(set(monitors))
    monitor_avg_lst = list(np.mean(readings[monitors == m])  for m in unique_monitors)
    high_monitor = str(unique_monitors[np.argmax(monitor_avg_lst)])
    
    monitor_avgs = np.mean(readings[monitors != high_monitor])
    monitor_offset = str(np.max(monitor_avg_lst) - monitor_avgs)

    other_readings = readings[monitors != high_monitor]
    stage2_other_monitors = str(np.sum(np.mean(other_readings, axis=1) >= 140))

    output = ("patients: " + patients + "\nreadings: " + total_readings + "\nmean_sbp: " + mean_sbp + "\nsd_sbp: " + sd_sbp + "\nmin_sbp: " + min_sbp + "\nmax_sbp: " + max_sbp + "\nstage2_patients: " + stage2_patients 
    + "\nhighest_patient: " + highest_patient + "\nhighest_patient_mean: " + highest_patient_mean + "\npeak_hour_column: " + peak_hour_column + "\npeak_hour_mean: " + peak_hour_mean + "\nhigh_monitor: " + high_monitor + "\nmonitor_offset: " + monitor_offset + "\nstage2_other_monitors: " + stage2_other_monitors)

    # TODO: write one "key: value" line per answer to output/vitals_summary.txt.
    with open("/Users/patricktse/Desktop/DATASCI217/ds217-26f-03/output/vitals_summary.txt", "w", encoding="utf-8") as output_file:
        output_file.write(output)

if __name__ == "__main__":
    main()
