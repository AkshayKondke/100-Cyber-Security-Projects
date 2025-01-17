# Project: Port Scanner Tool

## 📜 Overview
The **Port Scanner Tool** is a cybersecurity project designed to identify open ports on a given network host. Open ports indicate services running on a machine, and they can represent potential security vulnerabilities if not properly secured. This tool helps ethical hackers and system administrators analyze the security posture of their network by scanning for open ports efficiently.

---

## 🎯 Objectives
- Develop a Python-based tool to scan ports on a target host.
- Identify open ports and associated services.
- Learn networking fundamentals and Python libraries like `socket` and `argparse`.
- Implement multi-threading for faster port scanning.

---

## 🛠️ Core Concepts

### 1. **Ports and Services**
- **Ports:** Logical endpoints for network communication, identified by numbers (e.g., 80 for HTTP, 443 for HTTPS).
- **Open Ports:** Indicate active services that might be exploitable if misconfigured.

### 2. **Types of Ports**
- **Well-Known Ports (0–1023):** Commonly used by standard services (e.g., FTP, HTTP, SSH).
- **Registered Ports (1024–49151):** Used by specific applications.
- **Dynamic/Private Ports (49152–65535):** Used for temporary communication sessions.

### 3. **Reverse DNS Lookup**
- Resolves IP addresses to domain names, helpful in identifying the target's hostname.

### 4. **Multi-threading**
- Enhances scanning speed by concurrently scanning multiple ports using Python's `concurrent.futures.ThreadPoolExecutor`.

---

## 🔧 Tool Features
1. **Target Resolution**
   - Resolves a target domain to its corresponding IP address using `socket.gethostbyname()`.

2. **Port Scanning**
   - Scans a specified range of ports.
   - Detects open ports and retrieves associated service names using `socket.getservbyport()`.

3. **Threading**
   - Utilizes multi-threading for faster execution, allowing multiple ports to be scanned simultaneously.

4. **User Input**
   - Accepts target host, port range, and thread count as command-line arguments.

---

## 💻 Python Libraries Used
1. **`socket`**: For network communication and service resolution.
2. **`argparse`**: To handle command-line arguments.
3. **`concurrent.futures`**: For multi-threading and concurrent execution.

---

## 🧠 Learning Outcomes
- Understand the basics of networking and port communication.
- Gain experience with Python libraries for networking.
- Learn to implement efficient multi-threading in Python.
- Develop a practical cybersecurity tool for network analysis.

---

## 🚀 Future Enhancements
1. Add UDP port scanning capabilities.
2. Implement logging to save scan results to a file.
3. Integrate banner-grabbing functionality to identify running services.
4. Build a GUI version of the tool for non-technical users.

---

## ⚠️ Disclaimer
This tool is intended for educational purposes only. Ensure you have proper authorization before scanning any network or host.

