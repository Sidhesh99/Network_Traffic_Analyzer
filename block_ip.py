import os

def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    print(f"Blocked suspicious IP: {ip}")

block_ip("192.168.1.100")  # Change IP as needed
