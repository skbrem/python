correct_password = "Python123"
user_input = ""

user_input = input("Password: ")

attempts = 1

while user_input != correct_password and attempts < 3:
    print("Access denied, please try again.")
    attempts += 1
    user_input = input("Password: ")

if user_input == correct_password:
    print("Access granted")
else:
    print("Access denied")
