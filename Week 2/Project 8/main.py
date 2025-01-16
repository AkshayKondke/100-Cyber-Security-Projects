
import random


# datasets 

indian_first_names = ["Aarav","Sumit", "Vivaan", "Diya", "Ananya", "Ishaan", "Sneha", "Rohan", "Aditi"]
indian_last_names = ["Sharma", "Verma","Ubale", "Patel", "Gupta", "Reddy", "Das", "Chopra", "Mehta"]

foreign_first_names = ["James", "Sophia", "Liam", "Emma", "Oliver", "Isabella", "Noah", "Ava"]
foreign_last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis"]

def generate_random(number_of_names, region="both"):
    
    names = []

    for _ in range(number_of_names):
        if region == "indian":
            first_name = random.choice(indian_first_names)
            last_name = random.choice(indian_last_names)
        
        elif region == "foreign":
            first_name = random.choice(foreign_first_names)
            last_name = random.choice(foreign_last_names)

        else:
            if random.choice([True,False]):
                first_name = random.choice(indian_first_names)
                last_name = random.choice(indian_last_names)

            else :
                first_name = random.choice(foreign_first_names)
                last_name = random.choice(foreign_last_names)
            
        names.append(f"{first_name} {last_name}")   
    
    return names


def main():
    try:
        num_names = int(input("Enter the number of names you want to generate: "))
        region = input("Enter the region you want to generate names ('indian', 'foreign', 'both'): ").strip().lower()

        if num_names <= 0:
            print("Enter the positive number to generate the names : ")
        
        else:
            generate_names = generate_random(num_names, region)

            if generate_names :
                print("\nGenerated Names: ")

                for name in generate_names:
                    print(name)


    except ValueError :
        print(f"Please enter the valid number to generate the names !!")

if __name__ == "__main__":
    main()