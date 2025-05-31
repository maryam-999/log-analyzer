import sys

def analyze_logs():
    error_count = 0
    warning_count = 0
    info_count = 0

    with open("log.txt", "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    with open("rapport.txt", "w") as f:
        f.write(f"ERROR: {error_count}\n")
        f.write(f"WARNING: {warning_count}\n")
        f.write(f"INFO: {info_count}\n")

    print("Analyse terminée, voir rapport.txt")

    if error_count > 5:
        print("Trop d'erreurs détectées, échec du build")
        sys.exit(1)  # code d'erreur pour échec Jenkins

if __name__ == "__main__":
    analyze_logs()
