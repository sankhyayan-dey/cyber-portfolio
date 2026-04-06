# Live Cyber Threat Dashboard 🚨

A Python-based cybersecurity tool that fetches real-time vulnerability data from the National Vulnerability Database (NVD) and presents high-priority threats in a structured, analyst-friendly format.

This project simulates how Security Operations Center (SOC) teams monitor, filter, and prioritize vulnerabilities based on severity and risk.

---

## Project Overview

Modern systems are constantly exposed to newly discovered vulnerabilities. However, not all vulnerabilities require immediate attention.

This tool focuses on:

- Extracting **real-time CVE data**
- Filtering **HIGH and CRITICAL vulnerabilities**
- Presenting **actionable threat intelligence**
- Reducing noise for faster decision-making

---

## Features

- Live data fetching from NVD API
- Modular architecture (fetch -> parse -> display)
- Severity-based filtering (HIGH & CRITICAL)
- CVSS score integration for risk quantification
- CLI-based dashboard output
- Web-based dashboard (HTML, CSS, JavaScript)
- Clean and readable UI with severity visualization

---

## Tech Stack

- Python
- Requests (API handling)
- HTML, CSS, JavaScript
- JSON processing

---

## How It Works

1. **Data Fetching**
   - Retrieves latest vulnerabilities from NVD API
   - Uses a 7-day window to balance recency and data availability

2. **Data Parsing**
   - Extracts:
     - CVE ID
     - Severity
     - CVSS Score
     - Description

3. **Threat Filtering**
   - Keeps only **HIGH** and **CRITICAL** vulnerabilities
   - Eliminates low-impact noise

4. **Dashboard Output**
   - Displays:
     - Total vulnerabilities
     - Severity distribution
     - Detailed threat summaries

---

## Sample Output
```
============================================================
LIVE CYBER THREAT DASHBOARD
============================================================
Total High-Priority Vulnerabilities: 3
CRITICAL: 2
HIGH: 1

[1] CVE ID: CVE-2026-xxxx
Severity: HIGH (CVSS: 8.8)
Description: A vulnerability was determined in Wavlink...

[2] CVE ID: CVE-2025-xxxxx
Severity: CRITICAL (CVSS: 9.8)
Description: Amon2 versions before 6.17...

[3] CVE ID: CVE-2026-xxxx
Severity: CRITICAL (CVSS: 9.8)
Description: HTTP::Session versions through 0.53...
```

---

## Key Design Decisions

- **7-Day Time Window**
  - Avoids empty datasets (too narrow)
  - Avoids overload (too large)

- **Severity Filtering**
  - Focuses on HIGH & CRITICAL threats
  - Mimics real-world SOC prioritization

- **Modular Structure**
  - `fetch_data.py` - data retrieval
  - `parser.py` - processing & filtering
  - `main.py` - presentation layer
   - `dashboard/` - web interface  

---

## How to Run

```bash
pip install requests
cd src
python main.py

cd dashboard
open index.html
```