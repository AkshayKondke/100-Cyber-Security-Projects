

import pywifi
from pywifi import const
import time

def get_connected_network(iface):
    
    if iface.status() == const.IFACE_CONNECTED:
        profile = iface.network_profiles()[0]

        return {"ssid": profile.ssid, "bssid": "N/A", "signal": "N/A", "encryption": "SECURED"}

    return None

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    connected_network = get_connected_network(iface)

    print(f"Currently Connected Network: {connected_network['ssid'] if connected_network else 'None'}")

    iface.scan()
    time.sleep(2)

    networks = iface.scan_results()

    print("{:<25} {:<20} {:<10}".format("SSID", "BSSID", "Signal Strength", "Encryption"))

    print("-" * 70)

    if connected_network:
        print("{:<25} {:<20} {:<10} {}".format(
            connected_network["ssid"],
            connected_network["bssid"],
            connected_network["signal"],
            connected_network["encryption"],
            "(Connected)"

        ))

        for network in networks:
            ssid = network.ssid
            bssid = network.bssid
            signal = network.signal
            encryption = "OPEN" if network.akm[0] == const.AKM_TYPE_NONE else "SECURED"
            print("{:<25} {:<20} {:<10}".format(ssid, bssid, f"{signal} dBm", encryption))




def main():
    try:
        scan_wifi()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()