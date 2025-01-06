

import nmap
import json
import os



def result_save(results, filename="scan_results.json"):

    current_directory = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(current_directory, filename)


    try:
        with open(filename, "w") as file:
            json.dump(results, file, indent=4)
        print(f"Results save to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")




def scan(target, ports, scan_type):
    scanner = nmap.PortScanner()

    print(f"Scanning {target} on port range {ports} with scan type {scan_type}... ")

    try:
        scanner.scan(target, ports, scan_type)

        for host in scanner.all_hosts():
            print(f"\n Host: {host} ({scanner[host].hostname()})")
            print(f"\n State: {scanner[host].state()}")


            for protocol in scanner[host].all_protocols():
                print(f"Protocols: {protocol}")

                for port, info in scanner[host][protocol].items():
                    print(f"Port: {port}, State: {info['state']}")
        
        result_save(scanner._scan_result)

    except Exception as e:
        print(f"Error : {e}")


def main():
    target = input("Enter target (IP or hostname): ")
    ports = input("Enter port range (1-1024): ")
    print("Available scan type: \n -sS (SYN scan) \n -sT (TCP scan) \n -sU (UDP scan)")

    scan_type = input("Enter scan type (Default is -sS): ")

    scan(target, ports, scan_type)

if __name__ == "__main__":
    main()