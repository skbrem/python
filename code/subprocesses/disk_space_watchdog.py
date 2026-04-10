import subprocess
import sys

try:
    limit = int(sys.argv[1])
    print(f"Monitoring disk space with a {limit}% threshold.")
except:
    limit = 80
    print(f"No limit provided. Using default threshold of {limit}.")

raw_data = subprocess.check_output(["df", "-h"], text=True)

lines = raw_data.split("\n")

for line in lines:
    if line.endswith(" /"):
        parts = line.split()
        usage_string = parts[4]
        try:
            usage_number = int(usage_string.replace("%", ""))
            if usage_number > limit:
                print(f"CRITICAL ALERT: Usage is above 80%! Current usage is above {limit}%")
            else:
                print(f"Usage is below 80%")
        except Exception as e:
            print(f"Error: Could not evaluate disk space due to the following reason: {e}")
