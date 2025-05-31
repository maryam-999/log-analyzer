RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def analyze_logs():
    error_count = 0
    warning_count = 0
    info_count = 0

    with open("log.txt", "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
                print(f"{RED}{line.strip()}{RESET}")
            elif "WARNING" in line:
                warning_count += 1
                print(f"{YELLOW}{line.strip()}{RESET}")
            elif "INFO" in line:
                info_count += 1
                print(f"{GREEN}{line.strip()}{RESET}")

    with open("rapport.txt", "w") as f:
        f.write(f"ERROR: {error_count}\n")
        f.write(f"WARNING: {warning_count}\n")
        f.write(f"INFO: {info_count}\n")

    print("Analyse terminée, voir rapport.txt")
