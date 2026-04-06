from fetch_data import fetch_latest_vulnerabilities
from parser import parse_vulnerabilities


def main():
    raw_data = fetch_latest_vulnerabilities()

    if not raw_data:
        print("No data received.")
        return

    parsed_data = parse_vulnerabilities(raw_data)

    if not parsed_data:
        print("No high-priority vulnerabilities found.")
        return

    # 📊 Summary Counts
    total = len(parsed_data)
    critical_count = sum(1 for v in parsed_data if v["severity"] == "CRITICAL")
    high_count = sum(1 for v in parsed_data if v["severity"] == "HIGH")

    print("\n" + "=" * 60)
    print("🚨 LIVE CYBER THREAT DASHBOARD")
    print("=" * 60)

    print(f"Total High-Priority Vulnerabilities: {total}")
    print(f"CRITICAL: {critical_count}")
    print(f"HIGH: {high_count}")
    print("=" * 60)

    # 📋 Detailed Output
    for i, vuln in enumerate(parsed_data, start=1):
        print(f"\n[{i}] CVE ID: {vuln['cve_id']}")
        print(f"Severity: {vuln['severity']} (CVSS: {vuln['cvss_score']})")
        print(f"Description: {vuln['description'][:150]}...")
        print("-" * 60)


if __name__ == "__main__":
    main()