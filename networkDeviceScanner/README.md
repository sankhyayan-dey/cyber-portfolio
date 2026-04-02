# 🔍 Network Device Scanner

## 📌 Overview

The Network Device Scanner is a Python-based tool that discovers active devices on a local network using ARP scanning. It identifies devices by their IP and MAC addresses, detects manufacturers using MAC vendor lookup, and tracks changes by identifying new devices over time.

This project simulates a basic **network asset discovery and monitoring system**, commonly used in cybersecurity and IT infrastructure management.

---

## 🚀 Features

- 🔎 Scans local network for active devices
- 🌐 Retrieves IP and MAC addresses
- 🏭 Identifies device vendors (e.g., D-Link, AzureWave, Samsung)
- 🆕 Detects new vs known devices
- 📁 Saves scan results with timestamps (CSV format)
- 📊 Clean and readable terminal output

---

## 🛠️ Tech Stack

- Python
- Scapy (network scanning)
- Requests (API calls)
- CSV (data storage)

---

## ⚙️ How It Works

1. Sends ARP requests across the local network
2. Collects responses from active devices
3. Extracts IP and MAC addresses
4. Uses MAC vendor API to identify manufacturer
5. Compares with previous scans to detect new devices
6. Saves results for tracking and auditing

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/sankhyayan-dey/cyber-portfolio.git

# Navigate to project folder
cd networkDeviceScanner

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python src/scanNetworkDevices.py
```

## 📸 Sample Output

Scanning network... Please wait.

| IP Address    | MAC Address    | Vendor    | Status |
| ------------- | -------------- | --------- | ------ |
| 192.168.0.1   | xx:xx:xx:xx:xx | D-Link    | KNOWN  |
| 192.168.0.102 | xx:xx:xx:xx:xx | AzureWave | KNOWN  |

Scan complete. 2 device(s) found.<br>
Results saved to `data/scan_results_YYYY-MM-DD_HH-MM-SS.csv`

---

## 💡 Use Cases

- Detect unauthorized devices on a network
- Monitor network changes over time
- Maintain asset inventory
- Basic intrusion detection (new device alerting)

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.  
Use it only on networks you own or have permission to scan.

---

Built by **Sankhyayan Dey**
