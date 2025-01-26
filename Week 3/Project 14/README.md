# Wi-Fi Network Scanning Project 🚀

## Introduction 🌐
This project is a Python-based tool to scan nearby Wi-Fi networks and retrieve detailed information such as:
- SSID (Network Name)
- BSSID (MAC Address of the Access Point)
- Signal Strength (in dBm)
- Encryption Type (Open or Secured)

The tool also identifies the currently connected Wi-Fi network and displays it in the output.

---

## Features ✨
- Scan for available Wi-Fi networks in your area.
- Display signal strength and encryption status.
- Highlight the currently connected Wi-Fi network.
- User-friendly tabular output for better readability.

---

## Prerequisites 📋
Ensure you have the following installed:
- Python 3.10 or later 🐍
- Required Python Libraries:
  - `pywifi`
  - `time`

To install the necessary dependencies, run:
```bash
pip install pywifi
```

---

## How to Run 🏃‍♂️
1. Clone the repository:
   ```bash
   git clone https://github.com/AkshayKondke/100-Cyber-Security-Projects.git
   cd Week 3
   cd Project 14
   ```
2. Run the script:
   ```bash
   python main.py
   ```

---

## Output Format 📊
Here is a sample output:
```
Currently Connected Network: INTEX_14E1F0

Scanning for available Wi-Fi networks...

SSID                      BSSID                Signal Strength   Encryption
----------------------------------------------------------------------
INTEX_14E1F0             N/A                  N/A               SECURED    (Connected)
vivo v20 pro             d2:5a:dc:64:76:9c    -79 dBm           SECURED
DIRECT-yGLUCIFERmsJQ     16:d4:24:18:d0:bf    -78 dBm           SECURED
```

---

## Challenges Faced 🔧
1. **Driver Compatibility**:
   - Ensure your Wi-Fi adapter supports scanning features.

2. **Permissions**:
   - Running the script may require administrator privileges.

3. **Module Issues**:
   - Ensure all required Python modules are installed and up to date.

---

## Future Enhancements 🌈
- Add GUI support using libraries like Tkinter or PyQt.
- Export scan results to a file (CSV or JSON).
- Implement filtering options for networks based on SSID or signal strength.

---

## Contributing 🤝
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Coding! 💻

