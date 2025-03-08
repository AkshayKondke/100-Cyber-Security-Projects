import nmap
import argparse
import datetime

def scan_target(target, scan_type, output_file):
    nm = nmap.PortScanner()
    print(f"\n[🔍] Scanning target: {target} using {scan_type} scan...\n")
    
    try:
        if scan_type == "quick":
            nm.scan(hosts=target, arguments="-F")
        elif scan_type == "full":
            nm.scan(hosts=target, arguments="-sS -sV -O")
        elif scan_type == "vuln":
            nm.scan(hosts=target, arguments="--script vuln")
        else:
            print("[❌] Invalid scan type. Choose from: quick, full, vuln")
            return
        
        with open(output_file, "w") as f:
            scan_results = nm.csv()
            f.write(scan_results)
            
        print("\n[✅] Scan completed! Results saved to:", output_file)
        
    except Exception as e:
        print(f"[⚠️] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate Vulnerability Scanning with Nmap")
    parser.add_argument("target", help="Target IP or domain to scan")
    parser.add_argument("scan_type", choices=["quick", "full", "vuln"], help="Type of scan to perform")
    args = parser.parse_args()
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"nmap_scan_{args.target}_{timestamp}.csv"
    
    scan_target(args.target, args.scan_type, output_file)
