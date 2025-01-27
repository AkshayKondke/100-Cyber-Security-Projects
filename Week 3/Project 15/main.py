import base64
import sys

def encode_to_base64(input_string: str) -> str:
    
    try:
        encoded_bytes = base64.b16encode(input_string.encode("utf-8"))

        return encoded_bytes.decode("utf-8")

    except Exception as e:
        return f"Error during encoding: {e}."

def decode_from_base64(encoded_string: str) -> str:
    
    try:
        decoded_bytes = base64.b16decode(encoded_string.encode("utf-8"))

        return decoded_bytes.decode("utf-8")

    except Exception as e:
        return f"Error during decoding: {e}"

def file_handling():
    pass

def main():
    print("Base64 Encoder/Decoder Scripts")
    print("1. Encode a string to Base64.")
    print("2. Decode a Base64 string.")
    print("3. Exit.")

    while True:

        try:
            choice = int(input("\nEnter your choice (1-3):"))

            if choice == 1:
                input_string = input("Enter the string to encode: ")

                result = encode_to_base64(input_string)
                print(f"Encoded String: {result}")

            elif choice == 2:
                encoded_string = input("Enter the Base64 string to decode: ")

                result = decode_from_base64(encoded_string)
                print(f"Decoded String: {result}")

            elif choice == 3:
                print("Exiting... GoodBye!")
                sys.exit(0)
            
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
                

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    main()