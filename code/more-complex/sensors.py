import os
import time

LOG_DIR = "/var/log/sensor_data"
THRESHOLD = 35.0

sensor_readings = [
        {"timestamp": "12:00", "temperature": 22.5},
        {"timestamp": "12:05", "temperature": 24.1},
        {"timestamp": "12:10", "temperature": 36.8},
        {"timestamp": "12:15", "temperature": 38.2},
        {"timestamp": "12:20", "temperature": 31.0}
]

def check_system_alerts(reading_list):
    alert_count = 0

    print("Starting sensor data analysis...")
    print("-" * 30)

    for reading in reading_list:
        current_temp = reading["temperature"]
        current_time = reading["timestamp"]

        if current_temp > THRESHOLD:
            print(f"ALERT: High temperature detected at {current_time}! ({current_temp}°C)")
            alert_count += 1
        else:
            print(f"Status normal at {current_time}: {current_temp}°C")

    print("-" * 30)
    return alert_count

total_alerts = check_system_alerts(sensor_readings)
print(f"Analysis complete. Total critical events found: {total_alerts}")
