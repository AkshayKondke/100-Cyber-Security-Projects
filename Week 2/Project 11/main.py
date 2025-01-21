from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def generate_key(key_file="aes_key.key"):
    print("Generating Key...")
    print("\n")

    key = os.urandom(32)
    # print(key)

    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"Key saved to {key_file}.")
    print("\n")
    print("Key Generated...")



def load_key(key_file="aes_key.key"):
    
    with open(key_file, 'rb') as f:
        key = f.read()
    
    return key




def encrypt_file(input_file, output_file, key_file="aes_key.key"):
    print("File encrypting...")

    key = load_key(key_file)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)
    
    print("File Encrypted.")
    print(f"Saved to path = {output_file}")

def decrypt_file(input_file, output_file, key_file="aes_key.key"):
    print("Decrypting...")
    print("\n")

    key = load_key(key_file)
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(output_file, 'wb') as f:
        f.write(data)
    
    print("File Decrypted.")
    print(f"file saved path = {output_file}")


# /home/default/Desktop/nc/arsh.txt

def main():
    print("\n Welcome to file Encryption and Decryption Project \n")
    print("-"*70)
    print("\n")
    print("Instruction...\n")
    print("1.Generate key for Encrypting and Decrypting the files.\n")
    print("2. Encryption Input path- path/to/file.txt\n")
    print("3. Encryption output path - path/to/file.bin.\n")
    print("4. Decription Input path - path/to/file.bin.\n")
    print("5. Decryption output path - path/to/file.txt.\n")

    print("-"*70)
    print("\n")

    print("Choose an option: ")
    print("1. Generate Key.")
    print("2. Encrypt File")
    print("2. Decrypt File")
    print("\n")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        generate_key()

    elif choice == '2':
        input_file = input("Enter the path of file to encrypt: ").strip()
        output_file = input("Enter the output file path for the ecrypted file to save. ").strip()

        encrypt_file(input_file,output_file)

    elif choice == '3':
        input_file = input("Enter the path of the decrypt file: ").strip()
        output_file = input("Enter the output path of the file: ").strip()


        decrypt_file(input_file, output_file)
    
    else:
        print("\n")
        print("Invalid choice. Exiting...")
        



if __name__ == "__main__":
    main()