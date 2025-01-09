import email
from email import policy
from email.parser import BytesParser
import re
import dns.resolver
from prettytable import PrettyTable

# Function to parse email headers from a .eml file
def parse_email_headers(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    return msg

# Function to analyze SPF results
def analyze_spf(headers):
    spf_result = headers.get('Received-SPF', 'Not Found')
    return spf_result.strip()

# Function to analyze DKIM results
def analyze_dkim(headers):
    dkim_result = headers.get('Authentication-Results', 'Not Found')
    match = re.search(r'dkim=(\\w+)', dkim_result)
    return match.group(1) if match else "Not Found"

# Function to analyze DMARC results
def analyze_dmarc(headers):
    dmarc_result = headers.get('Authentication-Results', 'Not Found')
    match = re.search(r'dmarc=(\\w+)', dmarc_result)
    return match.group(1) if match else "Not Found"

# Function to trace the email route
def trace_email_route(headers):
    received_headers = headers.get_all('Received', [])
    return received_headers

# Function to display analysis results
def display_results(headers, spf, dkim, dmarc, route):
    # Display SPF, DKIM, and DMARC results in a table
    print("\n=== Email Header Analysis Results ===\n")
    table = PrettyTable()
    table.field_names = ["Check", "Result"]
    table.add_row(["SPF", spf])
    table.add_row(["DKIM", dkim])
    table.add_row(["DMARC", dmarc])
    print(table)

    # Display the email route trace
    print("\n=== Email Route Trace ===\n")
    for i, received in enumerate(route, start=1):
        print(f"Hop {i}: {received}\n")

# Main function to run the analyzer
def main():
    file_path = input("Enter the path to the .eml file: ")
    headers = parse_email_headers(file_path)

    spf_result = analyze_spf(headers)
    dkim_result = analyze_dkim(headers)
    dmarc_result = analyze_dmarc(headers)
    email_route = trace_email_route(headers)

    display_results(headers, spf_result, dkim_result, dmarc_result, email_route)

if __name__ == "__main__":
    main()
