import os
import platform
from concurrent.futures import ThreadPoolExecutor

def ping(ip):
    system = platform.system().lower()

    if system == "windows":
        command = f"ping -n 1 -w 200 {ip} > NUL"
    else:
        command = f"ping -c 1 -W 1 {ip} > /dev/null 2>&1"

    return os.system(command) == 0


def scan_network(base_ip):
    active_hosts = []

    def check(ip):
        if ping(ip):
            active_hosts.append(ip)

    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(1, 255):
            ip = f"{base_ip}.{i}"
            executor.submit(check, ip)

    return active_hosts