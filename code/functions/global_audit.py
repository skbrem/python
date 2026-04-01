def is_secure(password):
    if len(password) >= 8 and "!" in password:
        return True
    else:
        return False

migration_list = []
new_passwords = ["12345", "Password!", "Admin123", "SuperSecure!2026"]

for password in new_passwords:
    passwd = is_secure(password)
    if passwd:
        print("Valid")
        migration_list.append(password)
    else:
        print(f"Not valid")

print(f"Migration list complete: {migration_list}")
print(f"Total users to migrate: {len(migration_list)}")
      
