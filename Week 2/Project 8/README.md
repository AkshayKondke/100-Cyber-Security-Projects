# Random Name Generator 🎲

## Description 📝
The **Random Name Generator** is a Python script that generates random names based on the user's input. The script allows users to specify the number of names to generate and the region of the names: Indian, foreign, or both. It uses predefined datasets of first and last names for Indian and foreign regions to generate the names randomly.

## Features 🌟
- 🛠️ Generate a specified number of random names.
- 🌍 Choose the region for name generation: Indian, foreign, or a mix of both.
- ✅ Handles invalid inputs gracefully with error messages.

## Requirements 💻
- Python 3.x 🐍

## Usage 🚀
1. Run the script using Python:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the script file.

2. Follow the prompts:
   - 📌 Enter the number of names to generate (must be a positive integer).
   - 🌎 Specify the region:
     - `indian` for Indian names.
     - `foreign` for foreign names.
     - `both` for a mix of Indian and foreign names.

## Example 🎯
### Input:
```text
Enter the number of names you want to generate: 5
Enter the region you want to generate names ('indian', 'foreign', 'both'): both
```

### Output:
```text
Generated Names:
Diya Mehta
Liam Smith
Aarav Chopra
Sophia Johnson
Vivaan Patel
```

## Functions 📚

### 1. `generate_random(number_of_names, region="both")`
Generates a list of random names based on the given number and region.

#### Parameters:
- `number_of_names` (int): The number of names to generate.
- `region` (str): The region for name generation. Possible values are `indian`, `foreign`, and `both` (default).

#### Returns:
- A list of generated names as strings.

### 2. `main()`
The main entry point for the script. Handles user input, validation, and displays the generated names.

## Error Handling ⚠️
- If the user enters a non-positive number, a prompt requests a valid input.
- If the user enters an invalid number (e.g., letters or symbols), an error message is displayed.

## Datasets 📋
- **Indian Names:**
  - First Names: `Aarav, Sumit, Vivaan, Diya, Ananya, Ishaan, Sneha, Rohan, Aditi`
  - Last Names: `Sharma, Verma, Ubale, Patel, Gupta, Reddy, Das, Chopra, Mehta`

- **Foreign Names:**
  - First Names: `James, Sophia, Liam, Emma, Oliver, Isabella, Noah, Ava`
  - Last Names: `Smith, Johnson, Brown, Williams, Jones, Garcia, Miller, Davis`

## Customization ✨
You can add more names to the datasets by updating the `indian_first_names`, `indian_last_names`, `foreign_first_names`, or `foreign_last_names` lists in the script.

## License 📜
This project is licensed under the MIT License.

## Author ✍️
[Kondke Akshay]

---
Feel free to contribute or report any issues with this script! 💡

