# 🔒 File Encryption and Decryption Project

Welcome to the **File Encryption and Decryption Project**! This project allows you to securely encrypt and decrypt files using AES encryption. 🛡️

## 🚀 Features

- **AES Encryption with CBC Mode**
- Key generation for secure encryption/decryption 🔑
- File encryption with random initialization vector (IV) 🧩
- File decryption with PKCS7 padding removal ✅
- Simple and user-friendly CLI interface 🖥️

---

## 📁 Project Structure

```
📂 project-folder
 ├── aes_key.key          # Key file for encryption/decryption
 ├── input_file.txt       # Input file to encrypt
 ├── encrypted_file.bin   # Encrypted file output
 ├── decrypted_file.txt   # Decrypted file output
 ├── script.py            # Main Python script
```

---

## ⚙️ Requirements

Ensure you have the following installed on your system:

- Python 3.6 or higher 🐍
- `cryptography` library:
  ```bash
  pip install cryptography
  ```

---

## 📝 Instructions

### 1. Generate an Encryption Key 🔑
Run the script and select option `1` to generate a key:

```bash
python main.py
```

The key will be saved to a file named `aes_key.key`.

---

### 2. Encrypt a File 🛡️

Run the script and select option `2` to encrypt a file. Provide the input file path and the output file path for the encrypted file:

```bash
python main.py
```

Example inputs:
- Input file: `/path/to/input_file.txt`
- Output file: `/path/to/encrypted_file.bin`

---

### 3. Decrypt a File 🔓

Run the script and select option `3` to decrypt a file. Provide the encrypted file path and the output file path for the decrypted file:

```bash
python main.py
```

Example inputs:
- Encrypted file: `/path/to/encrypted_file.bin`
- Output file: `/path/to/decrypted_file.txt`

---

## 📌 Notes

- **Keep your key safe!** Losing the key means you cannot decrypt your files. 🗝️
- Ensure the key file (`aes_key.key`) is in the same directory as the script or provide the correct path.
- This script is intended for educational purposes. Avoid using it in production without thorough testing.

---

## 🛠️ Future Enhancements

- Add password-based encryption 🔑
- Improve error handling and validations 🚧
- Support for large file encryption 📂

---

## 👨‍💻 Author

Built with ❤️ by Akshay Kondke.

