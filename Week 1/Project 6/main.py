import hashlib
import os

def string_hash(input_string, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    hasher.update(input_string.encode('utf-8'))
    return hasher.hexdigest()

def file_hash(file_path=r"C:\Users\_akshay_0452\Downloads\sample1.json", algorithm='sha256'):
    hasher = hashlib.new(algorithm)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exists")

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
        return hasher.hexdigest()

def main():
    print("\n")
    print("\t \tWelcome! to Hashing Tools !!")
    print("________________________________________________________")
    print("\n")
    print("\n")

    print(f"1. Hashing a File \n2. Hashing a String")
    choice = input("Choose an option 1/2: ").strip()
    print("\n")
    print("\n")

    try:
        if choice == "1":
            print("You have choose to hash file.")
            file_path = input("Enter the file path: ")
            algorithm = input("Choose a algorithm : md5/sha256: ").lower().strip()
            try:
                print(f"{algorithm.upper()} Hash: {file_hash(file_path, algorithm)}")
            except FileNotFoundError as e:
                print(f"Error file not found! : {e}")
        
        elif choice == "2":
            print("You have choose to String file.")
            text = input("Enter the String: ")
            algorithm = input("Choose an Algorithm: md5/sha256: ").lower().strip()
            print(f"{algorithm.upper()} Hash: {string_hash(text, algorithm)}")
        else :
            print("Invalid Choose!")

    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()