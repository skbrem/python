numbers = 0

while True:
    num = int(input("Please type in integer number. Type in 0 to finish: "))
    if num == 0:
        break
    print(f"Number: {num}")
    numbers = num + 1

print(f"The program asks for numbers...")
print(f"Number: {num}")
print(f"Numbers typed in: {numbers}")

