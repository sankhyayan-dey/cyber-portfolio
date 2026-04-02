"""
Network Device Scanner

Features:
- Scans local network for active devices using ARP
- Retrieves IP and MAC addresses
- Identifies device vendors using an external API
- Saves scan results to CSV with timestamps
- Detects new vs known devices based on previous scans

Author: Sankhyayan Dey
"""

from scapy.all import ARP, Ether, srp
import requests
import os
import csv
from datetime import datetime


# Previous Scan Handling 

def loadPreviousScan():
    """
    Loads MAC addresses from the most recent scan file.
    Used to determine whether a device is NEW or KNOWN.
    """
    if not os.path.exists("data"):
        return []

    files = os.listdir("data")
    if not files:
        return []

    latestFile = sorted(files)[-1]
    previousDevices = []

    try:
        with open(f"data/{latestFile}", 'r') as file:
            next(file)  # Skip header row

            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    previousDevices.append(parts[1])  # MAC address
    except:
        return []

    return previousDevices


# Vendor Lookup

def getMacVendor(macAddress):
    """
    Fetches the vendor/manufacturer using MAC address.
    Uses macvendors API.
    """
    try:
        url = f"https://api.macvendors.com/{macAddress}"
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            return response.text
        return "Unknown"

    except:
        return "Error"


# Network Scanning

def scanNetwork(ipRange):
    """
    Scans the given IP range using ARP requests.
    Returns a list of active devices (IP + MAC).
    """

    # Create ARP request packet
    arpRequest = ARP(pdst=ipRange)

    # Broadcast to all devices in the network
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine ARP request with broadcast
    arpRequestBroadcast = broadcast / arpRequest

    # Send packet and receive responses
    answeredList = srp(arpRequestBroadcast, timeout=4, verbose=False)[0]

    devices = []

    for element in answeredList:
        deviceInfo = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        devices.append(deviceInfo)

    return devices


# Display Results

def displayDevices(devices):
    """
    Displays scanned devices in a formatted table.
    Also marks devices as NEW or KNOWN.
    """

    print("\n{:<18} {:<20} {:<25} {:<10}".format(
        "IP Address", "MAC Address", "Vendor", "Status"
    ))
    print("-" * 80)

    previousMacs = loadPreviousScan()

    for device in devices:
        vendor = getMacVendor(device['mac'])
        status = "NEW" if device['mac'] not in previousMacs else "KNOWN"

        print("{:<18} {:<20} {:<25} {:<10}".format(
            device['ip'],
            device['mac'],
            vendor,
            status
        ))

    print(f"\nScan complete. {len(devices)} device(s) found.")


# Save Results

def saveToCSV(devices):
    """
    Saves scan results to a CSV file with timestamp.
    """

    if not os.path.exists("data"):
        os.makedirs("data")

    fileName = f"data/scan_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    with open(fileName, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["IP Address", "MAC Address", "Vendor"])

        for device in devices:
            vendor = getMacVendor(device['mac'])
            writer.writerow([device['ip'], device['mac'], vendor])

    print(f"Results saved to {fileName}")


# Main Execution

if __name__ == "__main__":
    ipRange = "192.168.0.1/24"

    print("Scanning network... Please wait.\n")

    scannedDevices = scanNetwork(ipRange)

    displayDevices(scannedDevices)
    saveToCSV(scannedDevices)
    