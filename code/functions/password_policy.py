def is_secure(password):
    if len(password) >= 8 and "!" in password:
        return True
    else:
        return False

new_passwords = ["12345", "Password!", "Admin123", "SuperSecure!2026"]

for password in new_passwords:
    passwd = is_secure(password)
    if passwd:
        print(f"{password} is valid")
    else:
        print(f"{password} is invalid")

