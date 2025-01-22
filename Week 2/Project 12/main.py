
import subprocess
import re
import random


def generate_random_mac():
    print("\n")
    print("Generating new MAC Address...")

    return  ":".join([f"{random.randint(0x00, 0xFF):02x}" for _ in range(6)])

    # print(new)
    # return new

def get_current_mac(interface):
    try:
        
        result = subprocess.run(args=["ifconfig", interface], capture_output=True, text=True)

        mac_address = re.search(r"\b([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})\b", result.stdout)

        if mac_address:
            return mac_address.group(0)
        else:
            print(f"[WARNING] Could not read MAC Address for interface {interface}")

            return None
    except Exception as e:
        print(f"[ERROR] Failed to get MAC Address: {e}")

        return None

def change_mac(interface, new_mac):
    print("\n")
    print("Changing current mac address.")

    try:
        print(f"[INFO] Changing MAC Address of {interface} to {new_mac}...")

        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)

        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)

        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)

        print(f"[SUCCESS] MAC Address changed to {new_mac}")


    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to change MAC Address: {e}")

def main():
    print("-------MAC Address Changer---------")
    print("\n")
    
    interface = input("Enter the network interface (e.g., eth0, wlan0): ").strip()

    choice = input("Do you want to generate a random MAC Address? (yes/no): ").strip().lower()

    if choice == "yes":
        new_mac = generate_random_mac()
    else:
        new_mac = input("Enter the new MAC Address (format: xx:xx:xx:xx:xx:xx): ").strip()

    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"[INFO] Current MAC Address: {current_mac}")

    change_mac(interface, new_mac)


    # update mac 
    updated_mac = get_current_mac(interface)

    if updated_mac == new_mac:
        print(f"[SUCCESS] MAC Address successfully updated to {updated_mac}")
    else:
        print(f"[ERROR] MAC Address update failed. Current MAC is still {updated_mac}")
    

if __name__ == "__main__":
    main()