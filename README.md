# Network Lab Tools

Simple Python tool to scan a local network and detect active devices.

## Description

This project scans a local network (192.168.x.x) using ICMP ping requests and detects which devices are active.

It is designed for learning basic networking and Python automation.

## Features

- Detect local IP address
- Identify network range
- Scan all hosts in the subnet (1–254)
- List active devices
- Save results to a file

## How to use

Run the script:

```bash
python3 main.py


Output
Active IPs are shown in the terminal
Results are saved in results.txt
Requirements

No external dependencies required. Uses only Python standard library.

Disclaimer

This project is for educational purposes only and should be used only in your own network or lab environment.