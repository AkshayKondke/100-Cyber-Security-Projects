


def operation(text, shift, mode='encrypt'):
    result = ""
    # print(text)
    for char in text: 
        print(f"Processing char {char}") 
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')  
            shift_amount = shift if mode == 'encrypt' else -shift 
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            print(f"Shifted char: {new_char}")  
            result += new_char 
        else:
            print(f"Non-alphabetic char: {char}") 
            result += char  
            
    return result


def main():
    print("Ceaser-Cipher Encryption/Decryption")


    mode = input("Choose mode (Encrypt/Decrypt): ", ).strip().lower()

    if mode not in ['encrypt','decrypt']:
        print("Invalid mode , choose 'encrypt' or'decrypt'")
        return
    
    text = input("Enter the Text to encrypt/decrypt: ").strip()
    shift = int(input("Enter the shift value (1-25): ").strip())

    result = operation(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()