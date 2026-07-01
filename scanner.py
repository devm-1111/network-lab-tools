import os

def ping(ip):
    return os.system(f"ping -c 1 {ip} > /dev/null 2>&1") == 0

def scan_network(base_ip):
    active_hosts = []

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            active_hosts.append(ip)

    return active_hosts