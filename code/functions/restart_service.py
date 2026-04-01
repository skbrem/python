def restart_service(service_name):
    print(f"Shutting down {service_name}")
    print(f"Starting {service_name}")
    print(f"{service_name} is now ONLINE")

restart_service("Apache")
restart_service("MySQL")

