server_storage = {
    "FileSvr": 200,
    "AppSvr": 150,
    "Backup": 500
}

for name, size in server_storage.items():
    new_size = size + 50
    print(f"Updating {name}: Old size: {size}GB -> New Size: {new_size}GB")

print("Storage expansion completed")
