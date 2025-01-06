# 🔍 Network Scanner

A simple Python script that uses the `nmap` library to perform network scans and save the results in a JSON file.

## ✨ Features

- 🚀 Perform SYN, TCP, or UDP scans on a target IP or hostname.
- 🎯 Specify a custom port range for the scan.
- 💾 Save scan results to a JSON file for further analysis.

## ⚙️ Prerequisites

Ensure you have the following installed:

- 🐍 Python 3.6+
- 🛠️ `nmap` (Nmap must be installed on your system for the `python-nmap` library to work).

### 🧰 Python Libraries

Install the required Python library:

```bash
pip install python-nmap
```

## 🚀 Usage

1. 📥 Clone this repository or download the script file.
2. ▶️ Run the script using Python:

```bash
python network_scanner.py
```

3. 🛠️ Follow the prompts to:
    - 🔗 Enter the target (IP address or hostname).
    - 📡 Specify the port range (e.g., 1-1024).
    - ⚡ Choose a scan type (`-sS`, `-sT`, or `-sU`).

4. ✅ The script will display scan results in the console and save them to a `scan_results.json` file in the current directory.

## 📋 Example

```bash
Enter target (IP or hostname): 192.168.1.1
Enter port range (1-1024): 1-1024
Available scan type:
 -sS (SYN scan)
 -sT (TCP scan)
 -sU (UDP scan)
Enter scan type (Default is -sS): -sT
```

Output:

```
Scanning 192.168.1.1 on port range 1-1024 with scan type -sT...

Host: 192.168.1.1 (hostname_here)
State: up
Protocols: tcp
Port: 22, State: open
Port: 80, State: open

Results saved to scan_results.json
```

## 🗂️ File Structure

```
network_scanner.py  # Main script file
scan_results.json   # Output file generated after a scan
```

## 🚨 Error Handling

- ❌ The script handles exceptions for invalid inputs and scanning errors.
- 📄 Errors during file saving are also caught and displayed.

## ⚠️ Disclaimer

This tool is for educational purposes only. Ensure you have proper authorization before scanning any network or system.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
