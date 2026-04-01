server_count = 0
server_list = ""

current_entry = input("Please type in the current entry: ")

while current_entry != "done":
    server_list += current_entry + ", "
    server_count += 1
    current_entry = input("Please type in the current entry: ")

print(f"Here is the list of servers: {server_list}. Here is the number of servers is: {server_count}")
