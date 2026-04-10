import requests
import sys
import datetime


def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except:
        return "CONNECTION FAILED"

sites = ["https://codeberg.org", "https://github.com"]

if len(sys.argv) > 1:
    sites = [sys.argv[1]]

for site in sites:
    result = check_site(site)
    print(f"Site: {site} | Status: {result} | Health: {'Good' if result == 200 else 'Check server'}")
    if result != 200:
        now = datetime.datetime.now()strftime("%Y-%m-%d %H:%M:%S")
        with open("status_report.txt", "a") as f:
            f.write(f"[{now}] Error: {site} returned {result}\n")
        print(f"Error for {site} written to status_report.txt")
    else:
        print(f"{site} is healthy!")

