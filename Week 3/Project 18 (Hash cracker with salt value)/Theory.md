# 📖 Understanding PBKDF2 Password Cracker

## 🔹 Introduction
This document explains the theoretical concepts required to understand the **PBKDF2 Password Cracker** project. It covers the fundamentals of **hashing, salting, PBKDF2, dictionary attacks, and password cracking techniques**.

## 🔑 Key Concepts

### 1️⃣ **What is Hashing?**
Hashing is the process of converting an input (e.g., a password) into a fixed-length string using a cryptographic function. Hash functions are **one-way** and cannot be reversed. Examples include:
- **SHA-256**
- **MD5** (Insecure)
- **SHA-512**

### 2️⃣ **What is Salting?**
A **salt** is a random value added to a password before hashing. This prevents **rainbow table attacks** by ensuring that even identical passwords produce different hashes.

Example:
```
Password: password123
Salt: 5f4dcc3b5aa765d61d8327deb882cf99
Hashed Output: Different for each salt value
```

### 3️⃣ **PBKDF2 (Password-Based Key Derivation Function 2)**
PBKDF2 is a cryptographic key derivation function that **applies hashing multiple times (iterations)** to increase computational complexity, making brute-force attacks harder.

#### 🔹 How PBKDF2 Works:
1. Takes a **password**, **salt**, **iteration count**, and **key length** as inputs.
2. Uses **HMAC-SHA256** (or other hashing functions) for multiple iterations.
3. Produces a **derived key** that is resistant to brute-force attacks.

Formula:
```
DK = PBKDF2(HMAC, Password, Salt, Iterations, Key Length)
```

### 4️⃣ **Dictionary Attack**
A **dictionary attack** is a password-cracking technique that tries a list of common passwords (e.g., from `rockyou.txt`) against a target hash.

### 5️⃣ **How This Project Works**
1. User provides:
   - A **salt** (hex format)
   - A **target hash** (hex format)
   - A **dictionary file** containing potential passwords
2. The script:
   - Reads each password from the dictionary file
   - Hashes it using PBKDF2 with the given salt and iterations
   - Compares it to the target hash
3. If a match is found, the password is revealed.

### 6️⃣ **Security & Ethical Considerations**
- Always use **strong, unique passwords**.
- Use **multi-factor authentication (MFA)** for extra security.
- Never use this tool for unauthorized password cracking—it is **illegal** and **unethical**.

---

By understanding these core concepts, you can grasp how the **PBKDF2 Password Cracker** works and the importance of **secure password storage**. 🚀

Keep learning and stay secure! 🔒
```