import time
import csv
from data_providers import get_opensky_data
from conversion_intf import get_voltages

LOG_FILE = "voltages_log.csv"

# First run: write header
try:
    with open(LOG_FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "voltage_type1", "voltage_type2", "voltage_type3"])
except FileExistsError:
    pass  # already created

from data_providers import get_opensky_data
from conversion_intf import get_voltages

opensky_data = get_opensky_data(api)
voltages = get_voltages(opensky_data)
print(voltages)

alt_v, vel_v, dist_v = voltages

# Compute representative values (e.g. mean)
from statistics import mean
row = [
    time.time(),
    mean(alt_v) if alt_v else 0,
    mean(vel_v) if vel_v else 0,
    mean(dist_v) if dist_v else 0
]

# Write to CSV
with open(LOG_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)

