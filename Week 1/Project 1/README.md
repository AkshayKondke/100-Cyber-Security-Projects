# Password Generator 🔐

A Python script to generate random passwords based on user-specified criteria. This tool allows users to customize their passwords by choosing the length and the inclusion of uppercase letters, numbers, and special characters.

## Features ✨
- Generate passwords of user-defined length.
- Option to include or exclude:
  - Uppercase letters 🔠
  - Numbers 🔢
  - Special characters ❇️
- Validates input to ensure proper password generation.

## Prerequisites 🛠️
Make sure you have Python installed on your system. This script is compatible with Python 3.

## Usage 🖥️
1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Run the script using Python:
   ```bash
   python password_generator.py
   ```
4. Follow the on-screen prompts:
   - Enter the desired password length (must be greater than zero).
   - Specify whether to include uppercase letters, numbers, and special characters by typing 'y' (yes) or 'n' (no).
5. The generated password will be displayed on the screen.

## Example 📖
```
Enter the password Length: 12
Include Upper case? (y/n): y
Include number? (y/n): y
Include special character? (y/n): n
Generated password: pL2XhcjqdGh5
```

## Code Explanation 🧑‍💻
The script includes:
1. **`generate_password` function**:
   - Takes the password length and inclusion options as arguments.
   - Combines the selected character sets into a pool.
   - Randomly selects characters from the pool to create the password.

2. **Error handling**:
   - Ensures the password length is greater than zero.
   - Validates that at least one character type is selected.

## Error Messages ⚠️
- "Password length must be greater than zero."
- "No character type selected, Unable to generate."

## Dependencies 📦
This script uses Python's built-in `random` and `string` libraries. No additional installations are required.

## License 📝
This project is licensed under the MIT License.

## Author 👤
- [Your Name]
