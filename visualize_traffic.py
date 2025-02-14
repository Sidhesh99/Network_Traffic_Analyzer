import matplotlib.pyplot as plt

ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
traffic = [50, 200, 10]

plt.bar(ips, traffic)
plt.xlabel("Source IPs")
plt.ylabel("Packets Received")
plt.title("Network Traffic Analysis")
plt.show()
