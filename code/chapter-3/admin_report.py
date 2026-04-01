servers = ["Srv01:UP", "Srv02:UP", "Srv03:DOWN", "Srv04:UP", "Srv05:DOWN"]

down_count = 0

for server in servers:
    if ":DOWN" in server:
        down_count += 1

print(f"Check complete, total servers down: {down_count}")
