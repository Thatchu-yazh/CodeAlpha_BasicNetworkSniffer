# Developed by Thatchayaini R for CodeAlpha Internship

from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n==============================")
        print("      Packet Captured")
        print("==============================")
        print(f"Source IP        : {packet[IP].src}")
        print(f"Destination IP   : {packet[IP].dst}")
        print(f"Protocol Number  : {packet[IP].proto}")
        print(f"Packet Length    : {len(packet)} bytes")

print("====================================")
print(" CodeAlpha - Basic Network Sniffer ")
print("====================================")
print("Capturing 10 packets...\n")

sniff(prn=packet_callback, count=10)

print("\nCapture Complete!")