import socket
import os
import json


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_network_base(ip):
    return ".".join(ip.split(".")[:-1])


def ping(ip):
    return os.system(f"ping -n 1 -w 150 {ip} > NUL") == 0


def scan_network(base):
    active = []
    for i in range(1, 255):
        ip = f"{base}.{i}"
        if ping(ip):
            active.append(ip)
    return active


def main():
    ip = get_local_ip()
    base = get_network_base(ip)

    print("\n=== NETWORK INFO ===")
    print(f"Local IP: {ip}")
    print(f"Scanning network: {base}.0/24\n")

    devices = scan_network(base)

    results = []

    print("\n=== ACTIVE DEVICES ===")

    for d in devices:
        if d == "192.168.1.1":
            label = "Router"
        elif d == ip:
            label = "This device (YOU)"
        else:
            label = "Device"

        print(f"{d} - {label}")

        results.append({
            "ip": d,
            "type": label
        })

    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    main()