# Password Strength Checker 🔐

## Project Overview 🌟
The **Password Strength Checker** is a Python-based project designed to evaluate the strength of user-provided passwords. This tool helps users create stronger and more secure passwords by providing feedback and a detailed strength analysis.

---

## Features 🚀

- **Entropy Calculation**: Determines the randomness of the password based on its length and character set.
- **Strength Categorization**: Classifies passwords as **Weak**, **Moderate**, or **Strong**.
- **Pattern Detection**: Detects common patterns or weaknesses like repetitive characters or sequences.
- **Feedback System**: Provides actionable suggestions to improve password security.
- **Rich Visuals**: Uses the `rich` library to enhance the output with tables, panels, and colors.

---

## How It Works 🛠️
1. **User Input**: The user enters a password they want to evaluate.
2. **Entropy Calculation**: The script calculates the entropy based on the character sets used in the password.
3. **Weakness Detection**:
   - Checks for a minimum length of 8 characters.
   - Ensures the presence of lowercase, uppercase, numbers, and special characters.
   - Identifies common patterns or predictable passwords (e.g., "123456").
4. **Strength Evaluation**: Based on entropy, the password is categorized into one of three levels:
   - **Weak**: Entropy < 28 bits
   - **Moderate**: 28 ≤ Entropy < 36 bits
   - **Strong**: Entropy ≥ 36 bits
5. **Feedback and Report**: Displays a detailed analysis using a styled table and actionable feedback.

---

## Required Libraries 📦

Make sure you have the following Python libraries installed:

- `math` (built-in)
- `re` (built-in)
- `rich` (install via `pip`)

To install `rich`, run:
```bash
pip install rich
```

---

## Script Execution ▶️

1. Clone the repository or download the script.
2. Open a terminal in the script’s directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter your password when prompted and view the analysis.

---

## Example Output 📊

When you run the script, you’ll see output similar to the following:

```
╭───────────────────────────────────────────╮
│ Welcome to the Password Strength Checker! │
╰───────────────────────────────────────────╯
Enter your password to check its strength: [USER INPUT]

Password Strength Report

+----------------+----------------+
| Metric         | Value          |
+----------------+----------------+
| Password       | [USER INPUT]   |
| Strength       | Moderate       |
| Entropy        | 32.50 bits     |
+----------------+----------------+

Feedback:
- Add special characters (e.g., !@#$%).
- Use a longer password for better security.
```

---

## File Structure 📂

```
.
├── password_strength_checker.py   # Main script
├── README.md                      # Project documentation
├── Project_Theory.md              # Detailed theory and explanation
```

---

## Security Tips 🛡️

- Avoid using common passwords like "password123" or "123456."
- Use a combination of lowercase, uppercase, numbers, and special characters.
- Regularly update your passwords.
- Use a password manager to store and generate strong passwords.

---

## Why Password Strength Matters 🔑
Weak passwords are one of the leading causes of security breaches. By using this tool, you can:

- Protect your accounts from brute-force attacks.
- Enhance the overall security of your digital identity.
- Learn best practices for password creation.

---

## Contribute 🤝

Feel free to contribute to this project by:

- Suggesting improvements.
- Reporting bugs.
- Adding new features.

---

## License 📜
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

**Enjoy a safer digital experience with strong passwords! 🔒**

