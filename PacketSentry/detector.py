from collections import defaultdict
from datetime import datetime

from database import insert_alert

scan_tracker = defaultdict(set)

THRESHOLD = 5

def calculate_severity(port_count):

    if port_count >= 50:
        return "CRITICAL"

    elif port_count >= 20:
        return "HIGH"

    elif port_count >= 10:
        return "MEDIUM"

    else:
        return "LOW"


def detect_scan(src_ip, dst_port):

    scan_tracker[src_ip].add(dst_port)

    scanned_ports = len(scan_tracker[src_ip])

    print(f"[+] {src_ip} scanned port {dst_port}")

    if scanned_ports >= THRESHOLD:

        severity = calculate_severity(scanned_ports)

        timestamp = str(datetime.now())

        print("\n=================================")
        print("[ALERT] POSSIBLE SYN SCAN DETECTED")
        print(f"Attacker IP : {src_ip}")
        print(f"Ports Scanned : {scanned_ports}")
        print(f"Severity : {severity}")
        print(f"Timestamp : {timestamp}")
        print("=================================\n")

        insert_alert(
            src_ip,
            scanned_ports,
            severity,
            timestamp
        )
