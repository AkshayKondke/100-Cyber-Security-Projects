import requests
import time
from plyer import notification

# Function to check the availability of a website
def check_website(url):

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"✅ {url} is up!")
            return True
        
        else:
            print(f"⚠️ {url} returned status code {response.status_code}")
            return False
        

    except requests.exceptions.RequestException as e:
        print(f"❌ Error checking {url}: {e}")
        return False

# Function to send a desktop notification
def send_notification(title, message):

    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def monitor_websites(websites, check_interval):
    print("Starting Website Availability Checker... 🕵️")
    while True:
        for website in websites:
            is_up = check_website(website)
            if not is_up:
                send_notification("Website Down Alert!", f"{website} appears to be down! ❌")
        print(f"⏳ Waiting {check_interval} seconds before the next check...")
        time.sleep(check_interval)

def main():
    websites = [
        "https://example.com",
        "https://google.com",
        "https://tesla.com",
        "https://nonexistentwebsite.com"
    ]

    check_interval = 60

    monitor_websites(websites, check_interval)


if __name__ == "__main__":
    main()