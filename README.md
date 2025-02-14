# Network Traffic Analyzer using Python & Linux

A lightweight **Network Traffic Analyzer** built using **Python, Scapy, PyShark, and Linux tools**. This tool captures packets, detects **port scans** & **DDoS attacks**, logs suspicious activity, and **blocks malicious IPs** using `iptables`.  

## **Features**  
✅ **Packet Sniffing** – Capture live network traffic  
✅ **Port Scan Detection** – Identify potential attacks (e.g., Nmap scans)  
✅ **DDoS Detection** – Alert for high packet rates from single IPs  
✅ **Traffic Visualization** – Graphs using Matplotlib  
✅ **Automated IP Blocking** – Secure your network  

## Tech Stack
🔹 **Python** (Scapy, PyShark, Matplotlib)  
🔹 **Linux** (Ubuntu/Kali, tcpdump, iptables)  
🔹 **Wireshark** (for packet analysis)  

## How to Run 
```bash
# Install dependencies
sudo apt update
sudo apt install tcpdump wireshark -y
pip install scapy pyshark matplotlib

# Run Packet Sniffer
sudo python3 sniffer.py

# Run Port Scan Detector
sudo python3 detect_port_scan.py

# Run DDoS Detector
sudo python3 detect_ddos.py
