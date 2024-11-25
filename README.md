# DDNS_ATTACKS_AND_DEFENSES

This repository contains Python scripts demonstrating DNS spoofing and DNS amplification attacks using the `scapy` library. These scripts are for educational and research purposes only, to better understand DNS vulnerabilities and how to defend against them.

## Features

- **DNS Spoofing**: Responds to DNS queries with spoofed answers to redirect traffic to a malicious or unintended IP address.
- **DNS Amplification**: Exploits open DNS resolvers to flood a target IP with large amounts of DNS responses.

## Files

- `dns_spoof.py`: Implements a DNS spoofing attack by intercepting DNS queries and responding with forged packets.
- `dns_amplification.py`: Simulates a DNS amplification attack by sending spoofed DNS queries to an open resolver to flood the target victim.

## Requirements

- Python 3.x
- `scapy` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/dns-attack-scripts.git
   cd dns-attack-scripts
