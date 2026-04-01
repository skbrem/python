status = "REBOOTING"
attempts = 0

while status == "REBOOTING":
    attempts += 1
    print(f"Attempt {attempts}: Server still down")
    if attempts == 3:
        status = "ONLINE"

print(f"Server is up. Proceeding with deployment.")

