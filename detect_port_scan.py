from scapy.all import sniff
from collections import defaultdict

scan_attempts = defaultdict(int)

def detect_scan(packet):
    if packet.haslayer('IP') and packet.haslayer('TCP'):
        src_ip = packet['IP'].src
        dst_port = packet['TCP'].dport
        scan_attempts[(src_ip, dst_port)] += 1

        if scan_attempts[(src_ip, dst_port)] > 5:  # Threshold
            print(f"Potential Port Scan Detected from {src_ip} to Port {dst_port}")

sniff(iface="ens33", prn=detect_scan, store=False)  # Change eth0 if needed
