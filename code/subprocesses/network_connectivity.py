import subprocess
import sys

servers = ["google.com", "8.8.8.8", "this-is-a-fake-address.com"]

if len(sys.argv) > 1:
    servers = [sys.argv[1]]
    print(f"User specified target: {servers[0]}")

def check_ping(target):
    try:
        subprocess.run(["ping", "-c" "1", target], check=True, capture_output=True)
        return "SUCCESS"

    except subprocess.CalledProcessError:
        # In order to catch a specific error first
        return "FAILED"
    except Exception as e:
        # For any general errors like no internet connectivity
        return f"ERROR: {e}"

for server in servers:
    result = check_ping(server)
    print(f"Checking {server}... Result: {result}")
