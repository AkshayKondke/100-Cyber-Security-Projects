# Port Scanner

🔍 **A Python-based multithreaded port scanner** that checks for open ports on a specified target within a defined range. The script can identify the service associated with each open port, making it a useful tool for network administrators and security enthusiasts.

---

## ✨ Features

- 🧵 **Multithreading:** Utilizes `ThreadPoolExecutor` for fast and efficient scanning.
- 🔍 **Service Detection:** Identifies the service running on open ports when possible.
- 🎯 **Custom Port Range:** Allows users to define the range of ports to scan.
- ⚙️ **Custom Threads:** Lets users specify the number of threads for scanning.
- ⏱️ **Timeout Handling:** Includes timeouts for unresponsive ports.

---

## 🛠️ Requirements

- 🐍 Python 3.6 or higher

No additional libraries are required as the script uses only built-in Python modules.

---

## 🚀 How to Use

1. 📥 Clone the repository or copy the script to your local machine.
2. ▶️ Run the script using Python:

   ```bash
   python main.py
   ```

3. 🖥️ Enter the following inputs when prompted:

   - **Target IP or Domain:** The IP address or domain name of the target.
   - **Start Port:** The starting port number for the scan (default: 1).
   - **End Port:** The ending port number for the scan (default: 1024).
   - **Threads:** The number of threads to use (default: 50).

4. 📊 View the results of the scan directly in the terminal.

---

## 📋 Example Output

```text
Enter the target IP or domain: example.com
Enter the start port (Default 1): 20
Enter the end port (Default 1024): 25
Enter the number of threads (Default 50): 10

Target resolved example.com (93.184.216.34)
Scanning target 93.184.216.34 for open ports in range 20-25...

Port 21 : OPEN (ftp)
Port 22 : OPEN (ssh)
```

---

## 🔖 Notes

- ⚠️ **Error Handling:** If the target cannot be resolved, an error message will be displayed.
- ❓ **Unknown Services:** If a service is not recognized, it will be labeled as "Unknown Service."
- ⚖️ **Legal Usage:** Ensure you have explicit permission from the target owner before using this tool. Unauthorized port scanning may be illegal in some jurisdictions.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🤝 Contribution

Contributions are welcome! If you find a bug or have a suggestion, feel free to create an issue or submit a pull request.

