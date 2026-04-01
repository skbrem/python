tools = ["HelpDesk", "Email-Server", "Legacy-App", "Wiki"]

for tool in tools:
    try:
        if tool == "Legacy-App":
            raise ConnectionError
        print(f"Success. {tool} is responding.")
    except:
        print(f"Retry. {tool} timed out. Paging the On-Call Admin.")
    finally:
        print(f"[SYSTEM] Connection attempt for {tool} completed.")

