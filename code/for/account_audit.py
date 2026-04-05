users = [
    "admin_jm:IT:active",
    "user_js:Sales:active",
    "admin_sr:Eng:inactive",
    "user_bt:IT:inactive",
    "admin_kw:Ops:inactive"
]

flagged_accounts = 0

for user in users:
    if "admin" in user and "inactive" in user:
        print(f"SECURITY ALERT: Flagging {user} for review")
        flagged_accounts += 1

print(f"Total number of flagged accounts: {flagged_accounts}")

