attempts = 0

while attempts < 3:
    attempts += 1
    code = input("Enter admin key: ")
    if code == "STOP":
        break
    else:
        print(f"Attempt {attempts} recorded.")

print("System lock engaged")
