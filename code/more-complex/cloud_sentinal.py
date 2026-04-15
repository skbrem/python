import os
import logging

# api_key = os.getenv("CLOUD_API_KEY")

logging.basicConfig(
    filename='monitor.log',
    level=logging.INFO,
    format='%(asctime)s = %(levelname)s - %(message)s'
)

servers = [
    {"id": "i-001", "name": "DB-Master", "status": "running"},
    {"id": "i-002", "name": "Test-Box", "status": "stopped"},
    {"id": "i-003", "name": "Web-Server", "status": "stopped"}
]

stopped_count = 0

for server in servers:
    if server["status"] == "stopped":
        stopped_count += 1
        alert_msg = (f"Alert: {server['name']} (ID: {server['id']}) is stopped.")
        logging.info(alert_msg)
        print(alert_msg)

if stopped_count > 0:
    summary = f"Check complete: {stopped_count} stopped servers detected."
    logging.warning(summary)
    print(f"Summary: {summary}")
else:
    print(f"All systems operational")
