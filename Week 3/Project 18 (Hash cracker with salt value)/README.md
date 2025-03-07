# 🔐 PBKDF2 Password Cracker

## 📌 Overview
This project is a **PBKDF2-based Password Cracker** that attempts to recover a password using a dictionary attack. It uses **PBKDF2-HMAC-SHA256** with a given salt and iteration count to generate password hashes and compare them against a target hash.

## 🚀 Features
- Uses **PBKDF2-HMAC-SHA256** for secure password hashing.
- Supports **custom salts and iteration counts**.
- Reads from a **dictionary file** for brute-force attacks.
- Efficiently compares hashes to find the matching password.

## 📂 Project Structure
```
📁 PBKDF2-Password-Cracker
├── 📄 cracker.py   # Main script to perform the attack
├── 📄 README.md    # Project documentation
└── 📄 wordlist.txt # Sample dictionary file (not included, add your own)
```

## 🛠️ Installation & Usage

### 1️⃣ Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/PBKDF2-Password-Cracker.git
cd PBKDF2-Password-Cracker
```

### 3️⃣ Run the Script
```sh
python cracker.py
```

### 4️⃣ Provide Inputs
- **Salt (hex format)**: Example - `5f4dcc3b5aa765d61d8327deb882cf99`
- **Target Hash (hex format)**: The PBKDF2-derived hash you want to crack.
- **Dictionary File**: Path to a wordlist file (e.g., `rockyou.txt`).

### 5️⃣ Example Output
```
Enter the salt (hex format): 5f4dcc3b5aa765d61d8327deb882cf99
Enter the target hash (hex format): e99a18c428cb38d5f260853678922e03
Enter the dictionary file path: wordlist.txt

Checking password 1: password123
Checking password 2: qwerty
Checking password 3: letmein

[✅] Password Found: letmein
```

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to fork this repo, make improvements, and submit a **pull request**!

## 🛡️ Disclaimer
This tool is for **educational purposes only**. Unauthorized password cracking is **illegal** and **unethical**. Use this responsibly and only on systems you have permission to test.

---

🔗 **Follow Me**: [GitHub](https://github.com/AkshayKondke) | [LinkedIn](https://www.linkedin.com/in/akshay-kondke-12b07a246)

