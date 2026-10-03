# CodeAlpha Network Sniffer

A basic network packet sniffer in Python using Scapy, built for the CodeAlpha Cyber Security internship (Task 1).

## Features
- Captures live packets
- Shows source/destination IP, protocol (TCP/UDP/ICMP) and ports
- Shows a 40-byte payload preview
- Optional BPF filter from the command line

## Usage

    sudo python3 sniffer.py
    sudo python3 sniffer.py "icmp"
    sudo python3 sniffer.py "tcp port 443"

## Requirements
- Python 3
- Scapy: sudo apt install python3-scapy

## Note
Only use on networks you own or have permission to monitor.
