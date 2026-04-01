network_inventory = [
    "Web-01:UP", "Web-02:UP", "DB-01:DOWN",
    "Mail-01:UP", "Store-01:DOWN", "VPN-01:UP"
]

total_servers = len(network_inventory)
down_count = 0

for server_name in network_inventory:
    if ":DOWN" in server_name:
        print(f"ALERT: {server_name} is offline")
        down_count += 1
    else:
        print(f"{server_name} is responding")

up_count = total_servers - down_count

print(f"Total servers scanned: {total_servers}")
print(f"Total servers up: {up_count}")
print(f"Total servers down: {down_count}")
print(f"Server health: {up_count / total_servers * 100}")
