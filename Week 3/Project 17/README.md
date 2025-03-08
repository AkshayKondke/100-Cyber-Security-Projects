# 🔍 Automated Nmap Vulnerability Scanner

## 📌 Overview
This project automates **Nmap scanning** to analyze network security and detect vulnerabilities. It supports **quick, full, and vulnerability scans**, saving the results to a CSV file for further analysis.

## 🚀 Features
- **Quick Scan (-F)**: Fast scanning of commonly open ports.
- **Full Scan (-sS -sV -O)**: Comprehensive scanning with service and OS detection.
- **Vulnerability Scan (--script vuln)**: Runs vulnerability detection scripts.
- **Automatic CSV Report Generation**.

## 📂 Project Structure
```
📁 Nmap-Scanner
├── 📄 scanner.py   # Main script for scanning
├── 📄 README.md    # Project documentation
└── 📄 requirements.txt # Dependencies
```

## 🛠️ Installation & Usage

### 1️⃣ Prerequisites
Ensure you have **Python 3.x** and **Nmap** installed on your system.

#### Install Nmap (if not installed):
- **Linux/macOS**:
  ```sh
  sudo apt install nmap   # Debian/Ubuntu
  sudo yum install nmap   # CentOS/RHEL
  brew install nmap       # macOS (Homebrew)
  ```
- **Windows**:
  Download and install Nmap from [https://nmap.org/download.html](https://nmap.org/download.html)

#### Install Python Dependencies:
```sh
pip install python-nmap
```

### 2️⃣ Run the Script
```sh
python scanner.py <target> <scan_type>
```

#### Example Usage:
- **Quick Scan**: `python scanner.py 192.168.1.1 quick`
- **Full Scan**: `python scanner.py example.com full`
- **Vulnerability Scan**: `python scanner.py 192.168.1.1 vuln`

### 3️⃣ Output
The scan results are saved in a CSV file:
```
nmap_scan_192.168.1.1_YYYY-MM-DD_HH-MM-SS.csv
```

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to fork this repo, improve it, and submit a **pull request**!

## 🛡️ Disclaimer
This tool is for **educational and security research purposes only**. Unauthorized scanning of networks is **illegal**. Use this responsibly and only on networks you have permission to scan.

---

🔗 **Follow Me**: [GitHub](https://github.com/AkshayKondke) | [LinkedIn](https://www.linkedin.com/in/akshay-kondke-12b07a246)


