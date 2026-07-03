# Network Scanner Tool

A lightweight Python tool to scan a local network and detect active devices.

---

## Overview

This project scans a local area network (LAN) and identifies active devices using ICMP ping requests.

It automatically detects the local IP address and calculates the corresponding network range.

---

## Features

- Automatic local IP detection
- Network range calculation (/24 subnet)
- Active device discovery
- Simple command-line interface
- Works on Windows

---

## Example Output
Local IP: 192.168.1.245
Scanning network: 192.168.1.0/24

Active devices:

192.168.1.1 (Router)
192.168.1.202
192.168.1.237
192.168.1.245 (This device)


---

## Requirements

- Python 3.x

No external dependencies required.

---

## Usage

Clone the repository:

---

## Requirements

- Python 3.x

No external dependencies required.

---

## Usage

Clone the repository:

git clone https://github.com/devm-1111/network-lab-tools.git


Navigate to the project directory:

cd network-lab-tools


Run the program:

python main.py


---

## How it works

The tool sends ICMP echo requests (ping) to all IP addresses in the local subnet and checks which hosts respond.

Only active hosts are displayed in the output.

---

## Disclaimer

This tool is for educational purposes only.
It does not exploit, attack, or access devices.
It only detects devices that respond to network requests.
