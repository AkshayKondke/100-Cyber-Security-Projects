# MAC Address Changer 🖧

## Overview 📖
This Python script allows you to change the MAC (Media Access Control) address of your network interface. Changing your MAC address can be useful for privacy, testing, and troubleshooting purposes. The script provides an option to generate a random MAC address or specify a custom one. 🛠️

---

## Features ✨
- **Retrieve Current MAC Address**: Automatically fetches and displays the current MAC address of a specified network interface.
- **Generate Random MAC Address**: Creates a new, valid MAC address to use.
- **Change MAC Address**: Updates the MAC address of the specified network interface.
- **Error Handling**: Provides clear warnings and error messages for invalid inputs or failures.

---

## How It Works ⚙️
1. **Input Network Interface**: The script asks for the network interface name (e.g., `eth0`, `wlan0`).
2. **Choose MAC Address**:
   - Generate a random MAC address.
   - Provide a custom MAC address in the format `xx:xx:xx:xx:xx:xx`.
3. **Change the MAC Address**: The script will disable the network interface, apply the new MAC address, and re-enable it.
4. **Verification**: Confirms whether the MAC address was successfully updated.

---

## Requirements 🛠️
- Python 3.x
- Administrative privileges (root access).
- `ifconfig` utility installed (usually available on Linux).

---

## Installation 📥
1. Clone this repository:
   ```bash
   git clone https://github.com/AkshayKondke/100-Cyber-Security-Projects.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mac-address-changer
   ```
3. Ensure the script has execute permissions:
   ```bash
   chmod +x main.py
   ```

---

## Usage 🚀
1. Run the script:
   ```bash
   sudo python3 main.py
   ```
2. Follow the prompts to:
   - Enter the network interface name.
   - Choose whether to generate a random MAC address or input a custom one.

---

## Example 🎉
1. Start the script:
   ```bash
   sudo python3 main.py
   ```
2. Enter the network interface (e.g., `eth0`).
3. Choose to generate a random MAC address or provide one manually.
4. View the result:
   ```
   [INFO] Current MAC Address: 00:1a:2b:3c:4d:5e
   [INFO] Changing MAC Address of eth0 to aa:bb:cc:dd:ee:ff...
   [SUCCESS] MAC Address changed to aa:bb:cc:dd:ee:ff
   ```

---

## Note 📝
- This script is intended for **educational and testing purposes** only. Improper use may violate network policies or laws.
- Ensure you have the necessary permissions to run the script and modify network settings.

---

## Contributing 🤝
Feel free to fork this repository and submit pull requests. Suggestions and improvements are always welcome! 😄

---

## License 📜
This project is licensed under the MIT License.

---

## Disclaimer ⚠️
Use this tool responsibly. The author is not responsible for any misuse or damage caused by the use of this script.

---

