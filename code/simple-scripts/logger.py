server_list = ""
current_entry = ""

while current_entry != "done":
    current_entry = input("Enter down server (or done to finish): ")
    server_list += current_entry + ", "

print(f"Servers requiring maintenance: {server_list}")
