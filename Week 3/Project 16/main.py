import re
import math
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS+ SPECIAL_CHARACTERS


def calculate_entropy(password):
    
    charset_size = 0
    
    if any(char in LOWERCASE for char in password):
        charset_size += len(LOWERCASE)
    
    if any(char in UPPERCASE for char in password):
        charset_size += len(UPPERCASE)
    
    if any(char in DIGITS for char in password):
        charset_size += len(DIGITS)

    if any(char in SPECIAL_CHARACTERS for char in password):
        charset_size += len(SPECIAL_CHARACTERS)

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return entropy



def check_common_patterns(password):
    
    common_passwords = ["123456", "password", "123456789", "qwerty", "abc123"] 

    if password.lower() in common_passwords:
        return "Password is too common. Avoid using predictable passwords like '123456' or 'password'."
    
    if re.search(r"\d{4,}", password):
        return "Avoid long sequences of numbers"
    
    return None

def password_strength_checker(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")

    if not any(char in LOWERCASE for char in password):
        feedback.append("Add lowercase letters.")

    if not any(char in UPPERCASE for char in password):
        feedback.append("Add uppercase letters.")
    
    if not any(char in DIGITS for char in password):
        feedback.append("Include numbers.")
    
    if not any(char in SPECIAL_CHARACTERS for char in password):
        feedback.append("Use special characters (e.g., !@#$%).")

    
    common_pattern_feedback = check_common_patterns(password)
    
    if common_pattern_feedback:
        feedback.append(common_pattern_feedback)

    entropy = calculate_entropy(password)

    if entropy < 28:
        strength = "Weak"
    elif 28 <= entropy < 36:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return {
        "password": password,
        "strength": strength,
        "entropy": entropy,
        "feedback": feedback
    }
        

def main():
    
    console.print(Panel("[bold cyan] Welcome to the Password Strength Checker![/bold cyan]", expand=False))

    user_password = console.input("[bold yellow] Enter your password to check its strength: [/bold yellow]")

    result = password_strength_checker(user_password)

    # result = f"hello"

    console.print("\n [bold cyan] Password Strength Report[/bold cyan]", style="bold")

    table = Table(title="Password Analysis", box=box.SIMPLE)

    table.add_column("Metric", style="bold magenta")
    table.add_column("Value", style="bold green")


    table.add_row("Password", result['password'])
    table.add_row("Strength", result['strength'])
    table.add_row("Entropy", f"{result['entropy']:.2f} bits")

    console.print(table)

    if result['feedback']:
        console.print("[bold red]\n Feedback:[/bold red]", style="bold")

        for item in result['feedback']:
            console.print(f"- {item}", style="green")

    else:
        console.print("[bold green]\n Your password is strong and does not need improvement! [/bold green]")



if __name__ == "__main__":
    main()