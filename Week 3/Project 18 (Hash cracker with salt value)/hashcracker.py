import hashlib
import binascii

def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations,
        dklen
    )

def find_matching_password(dictionary_file, target_hash, salt, iterations=50000, dklen=50):
    target_hash_bytes = binascii.unhexlify(target_hash)  # Convert target hash from hex to bytes
    
    try:
        with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
            count = 0
            for line in file:
                password = line.strip()
                hash_value = pbkdf2_hash(password, salt, iterations, dklen)
                count += 1
                print(f"Checking password {count}: {password}")
                
                if hash_value == target_hash_bytes:
                    print(f"\n[✅] Password Found: {password}")
                    return password
            
            print("\n[❌] Password not found.")
            return None

    except FileNotFoundError:
        print("\n[❌] Error: Dictionary file not found! Check the file path.")
        return None

# 🔹 Get user input for hash cracking
salt_hex = input("Enter the salt (hex format): ").strip()
target_hash_hex = input("Enter the target hash (hex format): ").strip()
dictionary_file = input("Enter the dictionary file path: ").strip()

# Convert user inputs to bytes
try:
    salt = binascii.unhexlify(salt_hex)
    target_hash = target_hash_hex
except binascii.Error:
    print("\n[❌] Error: Invalid hex format! Ensure you enter correct hexadecimal values.")
    exit()

# 🔹 Run the password-cracking function
find_matching_password(dictionary_file, target_hash, salt)