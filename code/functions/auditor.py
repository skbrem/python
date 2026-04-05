import os

def scan_file(file_to_read, search_term):
    count = 0
    try:
        with open(file_to_read, "r") as f:
            for line in f:
                if search_term in line:
                    count += 1
        return count
    except:
        print(f"Error! Could not find the file {file_to_read}")
        return 0

alerts = scan_file("daily_report.txt", "Alert")
logins = scan_file("daily_report.txt", "Login")
print(f"I found {logins} login events.")
print(f"I found {alerts} critical alerts.")

files = os.listdir(".")

for file in files:
    if file.endswith(".txt"):
        found = scan_file(file, "Alert")
        print(f"Report for {file}: {found} alerts.")
