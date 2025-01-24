# 🌐 Website Availability Checker

## 📖 Overview
The **Website Availability Checker** is a Python-based tool designed to monitor the uptime of websites. It checks the availability of specified URLs, alerts the user if a website is down, and logs the results for better monitoring. 🚀

---

## 🎯 Features
- ✅ **Website Monitoring**: Checks the availability of multiple websites.
- 🔔 **Desktop Notifications**: Alerts users when a website is down.
- 📊 **HTTP Status Codes**: Verifies the HTTP response code of websites.
- 🔄 **Periodic Monitoring**: Performs checks at regular intervals.
- 💡 **Error Handling**: Handles network errors gracefully.

---

## 🛠️ Requirements
Make sure you have the following installed:

- Python 3.8 or higher 🐍
- Required Python libraries:
  ```bash
  pip install requests plyer
  ```

---

## 🚀 Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/website-availability-checker.git
   cd website-availability-checker
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:
   ```bash
   python website_checker.py
   ```

4. **Add Websites to Monitor**:
   - Edit the `websites` list in the `website_checker.py` file:
     ```python
     websites = [
         "https://example.com",
         "https://google.com",
         "https://nonexistentwebsite.com"
     ]
     ```

5. **Set the Check Interval**:
   - Adjust the `check_interval` variable to define how frequently (in seconds) websites should be checked:
     ```python
     check_interval = 60  # Check every 60 seconds
     ```

---

## 📝 Example Output
```
Starting Website Availability Checker... 🕵️
✅ https://example.com is up!
✅ https://google.com is up!
❌ Error checking https://nonexistentwebsite.com: HTTPSConnectionPool(host='nonexistentwebsite.com', port=443): Max retries exceeded.
⏳ Waiting 60 seconds before the next check...
```

---

## 📚 How It Works
1. The script uses the `requests` module to send HTTP GET requests to the specified websites.
2. If the website is reachable (`status_code == 200`), it logs a success message.
3. If the website is down or an error occurs, it logs an error and sends a desktop notification via the `plyer` library.
4. The process repeats at regular intervals defined by `check_interval`.

---

## 💡 Future Enhancements
- 🌟 Add email alerts for downtime notifications.
- 🌟 Implement a graphical user interface (GUI) using `tkinter`.
- 🌟 Log status changes to a file for historical analysis.
- 🌟 Add concurrency to monitor multiple websites simultaneously.

---

## 🧠 Skills Learned
- HTTP requests using Python's `requests` module.
- Exception handling in Python.
- Scheduling tasks using loops and delays.
- Sending desktop notifications using the `plyer` library.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss potential improvements. 🙌

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [Plyer Notifications](https://plyer.readthedocs.io/en/latest/)

---

## 🔗 Connect
For any queries or feedback, feel free to reach out:
- 🌐 [GitHub](https://github.com/AkshayKondke)
- ✉️ [Email](mailto:akshay.kondke999@gmail.com)
- 🔗 [LinkedIn](https://www.linkedin.com/in/akshay-kondke-12b07a246)

Happy Monitoring! 🚀

