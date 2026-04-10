import os
import shutil
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

backup_dir = "backups"

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

if os.path.exists("status_report.txt"):
    new_name = f"backup_{today}.txt"
    shutil.move("status_report.txt", f"backups/{new_name}")
    print(f"Success: Moved log to backups/{new_name}")
