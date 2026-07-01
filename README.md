# Network Scanner Tool (Python)

A simple Python tool to scan your local network and detect active devices.

## Features

- Detects your local IP automatically
- Identifies your local network range (/24)
- Scans active devices in the network
- Shows router and connected devices
- Works on Windows

## How it works

The tool gets your local IP address and scans all possible addresses in the same network (192.168.x.x) using ping requests.

Only devices that respond are shown as active.

## Requirements

- Python 3.x

No external libraries required.

## How to run

1. Clone the repository:
```bash

git clone https://github.com/devm-1111/network-lab-tools

Go into the folder:
cd network-lab-tools

Run the program:
python main.py


Example output
=== NETWORK INFO ===
Local IP: 192.168.1.245
Scanning network: 192.168.1.0/24

=== ACTIVE DEVICES ===
192.168.1.1
192.168.1.202
192.168.1.237
192.168.1.245
192.168.1.249

Disclaimer

This tool is for educational purposes only.
It does not hack, attack, or access any device. It only detects devices that respond to network requests.

Future improvements
Faster scanning using threads
Export results to JSON or TXT
Better device identification
Improved UI output