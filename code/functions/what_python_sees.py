import os

print(f"Current location: {os.getcwd()}")

print(f"Files I can see right now:")
print(os.listdir("."))

if os.path.exists("daily_report.txt"):
    print("Found it!")
else:
    pritn("Missing!")
