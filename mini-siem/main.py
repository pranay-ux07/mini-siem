from analyzer import analyze_logs, save_report

def main():
    print("🛡️ Mini SIEM Log Analyzer\n")

    file_path = input("Enter log file name (e.g., auth.log): ")

    alerts = analyze_logs(file_path)

    print("\nSecurity Report:\n")

    if not alerts:
        print("No major threats detected")
    else:
        for ip, attack, count in alerts:
            print(f"⚠️ {attack} from {ip} ({count} attempts)")

    save_report(alerts)
    print("\n📁 Report saved as report.csv")


if __name__ == "__main__":
    main()