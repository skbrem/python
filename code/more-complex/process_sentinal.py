import subprocess
import sys
import time
import os
import logging

logging.basicConfig(
    filename='monitor.log',
    level=logging.INFO,
    format='%(asctime)s = %(levelname)s - %(message)s'
)

if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <process_name> <threshold_percentage>")
    exit(1)

def send_notification(msg):
    pass

target = sys.argv[1]
threshold = float(sys.argv[2])

try:
    while True:
        os.system('clear')
        processes = 0
        total_memory = 0.0

        raw_output = subprocess.check_output(["ps", "aux"], text=True)
        lines = raw_output.split("\n")

        for line in lines:
            if not line: continue
            if target in line and sys.argv[0] not in line:
                processes += 1
                parts = line.split()
                try:
                    total_memory += float(parts[3])
                except (IndexError, ValueError):
                    continue
                
        if total_memory > threshold:
            error_msg = f"CRITICAL: {target} using {total_memory}"
            logging.warning(error_msg)
            send_notification(error_msg)
            print(f"\033[91m!!! WARNING: {total_memory:.2f}% !!!\033[0m")

        print(f"[{time.strftime('%H:%M:%S')}] {target}: {processes} proc(s) using {total_memory:.2f}% MEM")   
            
        time.sleep(5)

except KeyboardInterrupt:
    print(f"\nStopping Sentinel.")
    sys.exit(0)
