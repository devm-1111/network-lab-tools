import socket
import os

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
    print("Local IP:", ip)
    print("Scanning network:", base + ".0/24")

    print("\n=== ACTIVE DEVICES ===")
    devices = scan_network(base)

    for d in devices:
        print(d)

if __name__ == "__main__":
    main()