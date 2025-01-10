# Project: Script to Fetch WHOIS Information for a Domain

## Project Overview 🖥️
This project involves creating a Python script that retrieves WHOIS information for a given domain. The WHOIS protocol provides details about domain registration, such as the registrar, creation and expiration dates, and nameservers. This script is essential for cybersecurity professionals, domain administrators, and anyone managing internet resources.

---

## Objectives 🎯
- Automate the retrieval of WHOIS information for any domain.
- Extract and display important domain details in a user-friendly format.
- Handle errors gracefully, such as invalid domains or unresponsive WHOIS servers.

---

## Prerequisites 🛠️
Before starting this project, ensure you have the following knowledge and tools:

### 1. Technical Knowledge 📚
- **WHOIS Protocol**: Understand how WHOIS queries work and what kind of data is returned.
- **Networking Basics**: Familiarity with domain names, DNS, and IP addressing.
- **Python Basics**: Knowledge of Python programming, especially error handling and data parsing.
- **Regular Expressions (Regex)**: To parse and extract specific details from raw WHOIS data if needed.

### 2. Tools and Libraries 🧰
- Python 3.6+
- `python-whois` library
- A text editor or IDE for coding (e.g., VSCode, PyCharm)

---

## Installation ⚙️
1. Install Python:
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. Install the `whois` library:
   ```bash
   pip install python-whois
   ```

---

## Features of the Script ✨
- Fetches the following WHOIS details:
  - Domain Name
  - Registrar
  - Creation Date
  - Expiration Date
  - Last Updated Date
  - Status
  - Nameservers
- Error handling for:
  - Invalid domain inputs
  - Network issues
  - Missing WHOIS data

---

## How to Use 🚀
1. Run the script:
   ```bash
   python main.py
   ```
2. Input the domain name (e.g., `example.com`) when prompted.
3. The script will display the WHOIS information in a formatted manner.

---

## Example Output 📄
```
Enter the domain to fetch WHOIS information (e.g., example.com): example.com

WHOIS Information:
Domain Name: example.com
Registrar: Example Registrar
Creation Date: 1995-08-14
Expiration Date: 2025-08-14
Updated Date: 2023-01-01
Status: active
Nameservers: ns1.example.com, ns2.example.com
```

---

## Potential Enhancements 🚧
- Implement a GUI for easier user interaction.
- Add support for bulk WHOIS queries.
- Save the output to a file (e.g., CSV or JSON).
- Integrate with other tools for automated domain monitoring.

---

## References 📖
- [IANA WHOIS Service](https://www.iana.org/whois)
- Python `whois` Library Documentation
- [Introduction to WHOIS Protocol](https://en.wikipedia.org/wiki/WHOIS)

