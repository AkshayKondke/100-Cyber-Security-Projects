
def convert_len(value, from_unit, to_unit):
    
    length_conversion = {
        'meter' : 1,
        'kilometer' : 1000,
        'centimeter' : 0.01,
    }

    value_in_meter = value * length_conversion[from_unit]

    result = value_in_meter / length_conversion[to_unit]

    return int(result)


def convert_weigth(value, from_unit, to_unit):
    weight_conversion = {
        'gram' : 1,
        'kilogram': 1000,
        'milligram': 0.001
    }

    value_in_grams = value * weight_conversion[from_unit]

    result = value_in_grams / weight_conversion[to_unit]
    
    return int(result)


def convert_temp(value, from_unit, to_unit):
    
    if from_unit == "Cels" and to_unit == "Fahr":
        result = (value * 9/5) + 32
        return result
    
    elif from_unit == "Fahr" and to_unit == "Cels" :
        result = (value * 32) - 5/9
        return result
    
    else:
        return value
    
    

def main() :
    print("--------------------Welcome to the Unit Converter!--------------------- ")
    print("\n")


    choice = input("Choose type of conversion (Lenght, Weight, Temperature): ").lower()
    print("\n")

    if choice == "length":
        # print("lenght")
        value = float(input("Enter the value: "))
        from_unit = input("Enter the from unit (meter, kilometer, centimeter) : ").lower()
        to_unit = input("Enter the to unit (meter, kilometer, centimeter) : ").lower()
        result = convert_len(value, from_unit, to_unit)
        print(f"{value} {from_unit}, from unit is equal to {result} {to_unit}")
        print(f"------------{int(value)} {from_unit} = {result} {to_unit}")
    
    elif choice == "weight":
        print("weight")
        value = float(input("Enter the value: "))
        from_unit = input("Enter the from unit (gram, kilogram, milligram): ").lower()
        to_unit = input("Enter the to unit (gram, kilogram, milligram) : ").lower()
        result =convert_weigth(value, from_unit, to_unit)
        
        print(f"{value} {from_unit} from unit is equal to {result} {to_unit}.")

    
    elif choice == "temperature":
        print("temp")
        value = float(input("Enter the value: "))
        from_unit = input("Enter the from unit (Cels, Fahr): ").capitalize()
        to_unit = input("Enter the to unit (Cels, Fahr) : ").capitalize()
        result = convert_temp(value, from_unit, to_unit)
        
        print(f"{value} {from_unit} from unit is equal to {result} {to_unit}.")
        
    
    else :
        print("Invalid choice!!")


if __name__ == "__main__":
    main()