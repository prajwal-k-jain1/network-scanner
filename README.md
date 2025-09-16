# ARP-Scanner (Scapy)

A lightweight ARP network scanner written in Python using **Scapy**.  
It sends ARP requests on a given IP / subnet and lists live hosts with their MAC addresses.

> ⚠️ **Important:** This tool performs network discovery. Use it only on networks and machines you own or where you have explicit permission (lab/home networks, VMs). Do not run this against public or production networks.

---

## Features
- Send ARP requests to a single IP or a subnet (CIDR) and collect responses.
- Print discovered hosts in a simple IP ↔ MAC table.
- Minimal dependencies — only Scapy (works on Linux/macOS; on Windows requires Npcap + admin).

---

## Requirements
- Python
- [Scapy](https://scapy.net/) (`pip install scapy`)
- On Windows: install **Npcap** (WinPcap compatible) and run as Administrator.
- Recommended: run inside an isolated lab (VMs / host-only networks) for testing.

---

## Usage
```bash
# Single IP
python arp_scanner.py --ip 192.168.56.101

# Subnet (CIDR)
python arp_scanner.py --s 192.168.56.0/24
