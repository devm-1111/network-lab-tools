from utils import get_local_ip
from scanner import scan_network

def main():
    local_ip = get_local_ip()
    base_ip = ".".join(local_ip.split(".")[:-1])

    print(f"Local IP: {local_ip}")
    print(f"Scanning network: {base_ip}.0/24")

    devices = scan_network(base_ip)

    print("\nActive devices:")
    for device in devices:
        print(device)

    with open("results.txt", "w") as f:
        for device in devices:
            f.write(device + "\n")

if __name__ == "__main__":
    main()