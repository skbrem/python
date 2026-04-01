def get_health_status(cpu_percent):
    if cpu_percent > 90:
        return "OVERLOADED"
    else:
        return "STABLE"

cpu_logs = [45, 92, 78, 85, 30]

for cpu in cpu_logs:
    result = get_health_status(cpu)
    print(f"Reading {cpu}%. Status is {result}.")
