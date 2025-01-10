# WHOIS Information Gathering Tool

## Project Overview
This Python project allows users to retrieve and display WHOIS information for any given domain in a clean, readable format. It provides essential details such as the domain registrar, creation and expiration dates, status, and nameservers. This tool is especially useful for cybersecurity professionals and domain administrators.

---

## Features ✨
- Fetches detailed WHOIS information for a domain.
- Formats the output into a structured and user-friendly report.
- Handles errors gracefully (e.g., invalid domains or unresponsive WHOIS servers).
- Displays lists (like statuses and nameservers) neatly.

---

## Prerequisites 🛠️

1. **Python**: Install Python 3.6 or above from [python.org](https://www.python.org/downloads/).
2. **`python-whois` Library**: Install the necessary WHOIS library by running:
   ```bash
   pip install python-whois
   ```

---

## How to Use 🚀

1. Clone the repository:
   ```bash
   git clone https://github.com/AkshayKondke/100-Cyber-Security-Projects.git
   cd /Week 2/Project 7
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Enter the domain name (e.g., `example.com`) when prompted.

4. View the formatted WHOIS information report in the console.

---

## Example Output 📄
```
WHOIS Information Gathering Tool

Enter the Domain to fetch the WHOIS information (e.g., example.com): tesla.com

WHOIS Information Report:
========================================
Domain Name:
  example.com
----------------------------------------
Registrar:
  example, Inc.
----------------------------------------
Creation Date:
  1992-12-04 05:00:00
----------------------------------------
Expiration Date:
  2026-09-03 05:00:00
----------------------------------------
Updated Date:
  2024-10-04 10:15:20
----------------------------------------
Status:
  - clientDeleteProhibited
  - clientTransferProhibited
  - clientUpdateProhibited
  - serverDeleteProhibited
  - serverTransferProhibited
  - serverUpdateProhibited
----------------------------------------
Nameservers:
  - A1-125.AKaAM.NET
  - A10-467.AKAM.NET
  - A123-64.AKAM.NET
  - A238-65.AKAM.NET
----------------------------------------
```

---

## Potential Enhancements 🚧
- Add support for bulk WHOIS queries.
- Implement a GUI for easier use.
- Save WHOIS reports to files (e.g., JSON, CSV, or text).
- Integrate with other tools for automated domain monitoring.

---

## License 📜
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contribution 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.

---

## References 📖
- [IANA WHOIS Service](https://www.iana.org/whois)
- Python `whois` Library Documentation
- [Introduction to WHOIS Protocol](https://en.wikipedia.org/wiki/WHOIS)

