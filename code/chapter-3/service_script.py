service = {
    "Web": 400,
    "Database": 1200,
    "Cache": 200
}

for name, memory in service.items():
    if memory > 1000:
        print(f"ALERT: {name} is using too much RAM {memory}MB")

print("RAM audit complete")
