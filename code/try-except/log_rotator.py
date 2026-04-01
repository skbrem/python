logs = ["system.log", "auth.log", "missing_file.log", "kernel.log"]

with open("audit_results.txt", "w") as report:
    for log in logs:
        try:
            with open(log, "r") as f:
                report.write(f"{log}: FOUND\n")
        except:
            report.write(f"{log}: MISSING\n")

print("Log rotation audit finished.")
