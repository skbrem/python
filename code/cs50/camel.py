name = input("camelCase: ")

newname = ""

for c in name:
    if c.isupper():
        newname += f"_{c}".lower()
    else:
        newname += c

print(f"snake_case: {newname}")
