# 🌐 Website Availability Checker

## 📝 Project Overview
The "Website Availability Checker" is a Python-based project designed to monitor the uptime of websites and alert users when a website becomes unavailable. This tool is valuable for ensuring website reliability and addressing downtime promptly.

---

## ⭐ Key Features
1. **🔍 Website Monitoring**: Check the availability of specified websites.
2. **📊 HTTP Status Code Analysis**: Verify the HTTP response code to determine the site's status.
3. **⚙️ Error Handling**: Handle network errors and invalid URLs gracefully.
4. **🔔 Alerts**: Notify users via console messages, email, or desktop notifications.
5. **⏲️ Scheduled Checks**: Perform periodic checks using loops or scheduling libraries.
6. **🗂️ Logs**: Maintain a record of website status changes for analysis.

---

## 📚 Concepts and Knowledge
To build this project, the following concepts are essential:

### 1. 🌐 HTTP/HTTPS Basics
- **HTTP** (HyperText Transfer Protocol) and **HTTPS** (secure version) govern web communication.
- **HTTP Status Codes**:
  - `200 OK`: ✅ Website is accessible.
  - `404 Not Found`: ❌ Page does not exist.
  - `500 Internal Server Error`: ⚠️ Server-side issue.
  - `503 Service Unavailable`: ⏳ Temporary server downtime.

### 2. 🐍 Python’s `requests` Module
- **Installation**: Install using `pip install requests`.
- **Basic Syntax**:
  ```python
  import requests
  response = requests.get("https://example.com")
  print(response.status_code)
  ```
- **Timeouts**:
  ```python
  response = requests.get("https://example.com", timeout=5)
  ```

### 3. 🛠️ Error Handling
- Handle exceptions for scenarios like:
  - 🌐 Network errors.
  - ❌ Invalid URLs.
  ```python
  try:
      response = requests.get("https://example.com", timeout=5)
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```

### 4. ⏳ Scheduling and Loops
- Use loops for periodic website checks.
- Libraries like `schedule` or `time` can help:
  ```python
  import time
  while True:
      # Perform the check
      time.sleep(60)  # Wait for 1 minute
  ```

### 5. 🔔 Notifications
- **🖥️ Console Logs**: Simple print statements.
- **📧 Email Alerts**: Use `smtplib` or third-party services like SendGrid.
- **💻 Desktop Notifications**: Use libraries like `plyer`.

### 6. 🚀 Optional Enhancements
- **⚡ Concurrency**: Use `threading` or `asyncio` for monitoring multiple sites simultaneously.
- **📝 Logging**: Use the `logging` module for detailed records.
- **📊 Dashboard**: Build a graphical interface using `tkinter` or `Flask`.

---

## 🛠️ Implementation Steps

### Step 1: 🖥️ Setup Environment
1. Install Python (>= 3.8).
2. Install necessary libraries:
   ```bash
   pip install requests schedule plyer
   ```

### Step 2: 🔍 Basic Website Check
Write a script to fetch the HTTP status code of a website.

### Step 3: ⚙️ Add Error Handling
Handle scenarios like timeout or invalid URLs.

### Step 4: 🔔 Implement Notifications
Add email or desktop notifications for downtime alerts.

### Step 5: ⏲️ Schedule Regular Checks
Use loops or the `schedule` library to automate periodic checks.

### Step 6: 🧪 Test and Enhance
Test the script with various websites and edge cases. Add optional features like logging or a user interface.

---

## 💻 Example Code Snippet
```python
import requests
import time

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is up! ✅")
        else:
            print(f"{url} returned status code {response.status_code} ⚠️")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e} ❌")

if __name__ == "__main__":
    website = "https://example.com"
    while True:
        check_website(website)
        time.sleep(60)  # Check every 60 seconds
```

---

## 🧠 Skills Learned
- 🌐 HTTP requests and status codes.
- 🛠️ Exception handling in Python.
- ⏲️ Scheduling tasks in Python.
- 🔔 Sending notifications using Python libraries.

---

## 📅 Completion Date
_24/01/2025_

---

## 📝 Notes
_Cyber Security Educational Project_

