import random
import string

def generate_password(length, use_uppercase, use_number, use_special):
    
    character = string.ascii_lowercase
    
    if use_uppercase:
        character += string.ascii_uppercase
    
    if use_number :
        character += string.digits
    
    if use_special:
        character += string.punctuation

    if not character:
        raise ValueError("No character type selected, Unable to generate.")
    

    password = ''.join(random.choice(character) for _ in range(length))
    return password


try :
    length = int(input("Enter the password Length: "))

    if length <= 0 :
        raise ValueError("Password length must be greater than zero.")
    
    use_uppercase = input("Include Upper case? (y/n): ").strip().lower() == 'y'
    use_number = input("Include number? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special character? (y/n) : ").strip().lower() == 'y'



    password = generate_password(length, use_number, use_special, use_uppercase)
    print(f"Generated password : {password}")

except ValueError as e :
    print(f"Error: {e}")    