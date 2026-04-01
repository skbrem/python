disk_usage = {
    "Srv-01": 80,
    "Srv-02": "Unknown",
    "Srv-03": 40
}

for name, cpu in disk_usage.items():
    try:
        remaining = 100 - cpu
        print(f"{name} has {remaining} left.")
    except:
        print(f"Alert! Could not read the data for {name}")
