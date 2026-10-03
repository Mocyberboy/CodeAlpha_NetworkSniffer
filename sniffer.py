from scapy.all import sniff, IP, TCP, UDP, Raw

def show(packet):
    if IP not in packet:
        return

    src = packet[IP].src
    dst = packet[IP].dst
    proto = packet[IP].proto

    if TCP in packet:
        name = "TCP"
        ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
    elif UDP in packet:
        name = "UDP"
        ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
    elif proto == 1:
        name = "ICMP"
        ports = "-"
    else:
        name = str(proto)
        ports = "-"

    print(f"{src} -> {dst} | {name} | ports: {ports}")

    if Raw in packet:
        data = bytes(packet[Raw].load)[:40]
        print("   payload:", data)

import sys
flt = sys.argv[1] if len(sys.argv) > 1 else ""
sniff(filter=flt, count=20, prn=show)
