status_code = 0

while status_code == 0:
    print("System healthy... checking again")
    status_code = int(input("Please input a status code: "))

print("Critical error: System has halted")
