logs = ["OK", "Error", "OK", "OK", "Error"]

for alerts in logs:
    if alerts == "Error":
        print("ALERT: Found an error in the logs!")

print("Log scan complete.")
