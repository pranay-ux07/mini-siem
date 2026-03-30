from collections import defaultdict
from utils import extract_ip
import config
import csv

def analyze_logs(file_path):
    failed_attempts = defaultdict(int)
    success_logins = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:

                ip = extract_ip(line)
                if not ip:
                    continue

                if "Failed password" in line:
                    failed_attempts[ip] += 1

                elif "Accepted password" in line:
                    success_logins[ip] += 1

    except FileNotFoundError:
        print("Log file not found!")
        return

    alerts = []

    for ip in failed_attempts:
        failed = failed_attempts[ip]
        success = success_logins[ip]

        if failed >= config.BRUTE_FORCE_THRESHOLD:
            alerts.append((ip, "Brute Force Attack", failed))

        elif failed >= config.SUSPICIOUS_THRESHOLD and success == 0:
            alerts.append((ip, "Suspicious Activity", failed))

    return alerts


def save_report(alerts):
    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Attack Type", "Failed Attempts"])

        for alert in alerts:
            writer.writerow(alert)