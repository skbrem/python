cloud_servers = [
    {"name": "Web-01", "cpu": 45, "ip": "10.0.0.1"},
    {"name": "DB-01", "cpu": 92, "ip": "10.0.0.2"},
    {"name": "Mail-01", "cpu": 78, "ip": "10.0.0.3"},
    {"name": "Proxy-01", "cpu": 85, "ip": "10.0.0.4"}
]

for server in cloud_servers:
    if server["cpu"] > 80:
        print(f"Ticket created: {name} at {ip} is running at {cpu}% CPU")

print(f"Audit of all of the {len(cloud_servers)} servers completed.")
