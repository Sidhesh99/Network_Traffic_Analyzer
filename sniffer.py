from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Print packet details

sniff(iface="ens33", prn=packet_callback, store=False)  # Change eth0 if needed
