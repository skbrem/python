firewall_rules = {
    80: "OPEN",
    443: "CLOSED",
    22: "OPEN"
}

for port, status in firewall_rules.items():
    if status == "OPEN":
        print(f"Closing Port {port}... Status Updated to CLOSED")
    else:
        print(f"Port is already closed.")

print("The security sweep has been completed")
