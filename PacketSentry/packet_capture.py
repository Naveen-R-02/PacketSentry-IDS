from scapy.all import sniff, IP, TCP
from detector import detect_scan

TARGET_IP = "10.215.52.146"

def process_packet(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        dst_port = packet[TCP].dport

        tcp_flags = packet[TCP].flags

        # SYN packet detection
        if dst_ip == TARGET_IP and tcp_flags & 0x02:

            print(f"[SYN] {src_ip} -> {dst_ip}:{dst_port}")

            detect_scan(src_ip, dst_port)

def start_sniffing():

    print("[+] PacketSentry IDS Started...\n")

    sniff(
        iface="eth0",
        filter="tcp",
        prn=process_packet,
        store=False
    )
