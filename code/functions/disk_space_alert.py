def check_disk(percent_used):
    if percent_used > 90:
        return "CRITICAL"
    else:
        return "HEALTHY"

status = check_disk(95)
print(f"The server status is: {status}")
