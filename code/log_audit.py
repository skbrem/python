logs = ["OK", "OK", "Error", "OK", "Error", "Error"]

error_count = 0

for error in logs:
    if error == "Error":
        error_count += 1

print(f"Total errors found: {error_count}")
