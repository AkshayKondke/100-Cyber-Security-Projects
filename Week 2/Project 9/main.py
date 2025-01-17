

import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port):
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.settimeout(1)
            soc.connect((target, port))

            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown Service"

            print(f"Port {port} : OPEN ({service}) ")

    except (socket.timeout, ConnectionRefusedError):
        # print("error")
        pass


def scan_ports(target, start_port, end_port, threads):
    print(f"Scanning target {target} for open ports in range {start_port}-{end_port}...\n")
    with ThreadPoolExecutor(max_workers=threads) as excutor:
        for port in range (start_port, end_port + 1):
            excutor.submit(scan_port, target, port)


def main():
    target = input("Enter the target IP or domain: ")
    start_port = int(input("Enter the start port (Default 1): ") or 1)
    end_port = int(input("Enter the end port (Default 1024): ") or 1024)
    threads = int(input("Enter the number of threads (Default 50): )") or 50)


    try:
        target_ip = socket.gethostbyname(target)
        print(f"Target resolved {target} ({target_ip})")

        scan_ports(target_ip, start_port, end_port, threads)
    except socket.gaierror:
        print(f"Error: Unable to resolve {target}")


if __name__ == "__main__":
    main()