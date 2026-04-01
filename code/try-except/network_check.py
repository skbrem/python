devices = ["192", "168", "offline", "254"]

for device in devices:
    try:
        ip_num = int(device)
        print(f"Success. Device {ip_num} is registered")
    except:
        print(f"Error. Could not register device {device}. Skipping...")

print("Network scan complete.")
