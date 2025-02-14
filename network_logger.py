import logging

logging.basicConfig(filename="network_log.txt", level=logging.INFO)

def log_suspicious_activity(activity):
    logging.info(activity)

log_suspicious_activity("Potential Port Scan Detected from 192.168.1.10 to Port 22")
