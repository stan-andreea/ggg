import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV log
try:
    df = pd.read_csv("voltages_log.csv", header=None)
except FileNotFoundError:
    print("Error: voltages_log.csv not found.")
    exit(1)

# Name the columns
df.columns = ["timestamp", "alt_voltage", "vel_voltage", "dist_voltage"]

# Convert timestamps to datetime for readable x-axis
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df["timestamp"], df["alt_voltage"], label="Altitude Voltage", marker='o')
plt.plot(df["timestamp"], df["vel_voltage"], label="Velocity Voltage", marker='s')
plt.plot(df["timestamp"], df["dist_voltage"], label="Distance Voltage", marker='^')

# Customize plot
plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.title("Voltages Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot to image
plt.savefig("voltages_plot.png")
print("Plot saved as voltages_plot.png")
