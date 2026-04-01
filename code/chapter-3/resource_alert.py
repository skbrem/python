disk_space = 100

while disk_space >= 20:
    print(f"The current disk space is: {disk_space}")
    log_file = int(input("Please enter the size of the log file to save (In GB): "))
    disk_space -= log_file

print(f"Warning: Low disk space! Remaining disk space is {disk_space}GB")
print(f"Cleaning up temporary files")
