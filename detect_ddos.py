from scapy.all import sniff
from collections import Counter
import time

packet_count = Counter()
start_time = time.time()

def detect_ddos(packet):
    global start_time
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        packet_count[src_ip] += 1

    if time.time() - start_time > 10:
        for ip, count in packet_count.items():
            if count > 100:  # Threshold for DDoS detection
                print(f"Possible DDoS attack from {ip} - {count} packets received!")
        packet_count.clear()
        start_time = time.time()

sniff(iface="ens33", prn=detect_ddos, store=False)  # Change eth0 if needed
