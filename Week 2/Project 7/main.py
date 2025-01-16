import whois
from datetime import datetime

def format_date(date):
    if isinstance(date, list):
        return ', '.join([d.strftime('%Y-%m-%d %H:%M:%S') for d in date if d])
    elif isinstance(date, datetime):
        return date.strftime('%Y-%m-%d %H:%M:%S')
    return str(date)

def format_list(items):
    if isinstance(items, list):
        return '\n  - ' + '\n  - '.join(items)
    return items

def fetch_whois(domain):
    try:
        domain_info = whois.whois(domain)
        # print(domain_info)
        return {
            'Domain Name': domain_info.domain_name,
            'Registrar': domain_info.registrar,
            'Creation Date': format_date(domain_info.creation_date),
            'Expiration Date': format_date(domain_info.expiration_date),
            'Updated Date': format_date(domain_info.updated_date),
            'Status': format_list(domain_info.status),
            'Nameservers': format_list(domain_info.name_servers),
        }
    except Exception as e:
        print(f"Error occured while fetching : {e}")


def main():
    print("\n")
    print("WHOIS Information Gathering Tool.")
    print("\n")
    domain = input("Enter the Domain to fetch the WHOIS information (ex. example.com): ")

    whois_data = fetch_whois(domain)

    print("\n WHOIS Information: ")
    print("*" * 40)

    for key, value in whois_data.items():
        print(f"{key} : {value}")
        print("*" * 40)


if __name__ == "__main__":
    main()