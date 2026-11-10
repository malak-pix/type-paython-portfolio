# security_toolkit.py
# Security Toolkit - main program with a menu:
# 1. Check a port: tells if port is system, user, dynamic or invalid
# 2. Check a password: must be at least 8 chars and different from username
# 3. PIN guessing time: calculates days to guess a PIN
# q quits and shows how many checks were done.

MIN_LENGTH = 8

def border(text):
    """Print text inside [ ... ]."""
    print(f"[ {text} ]")

def show_menu():
    """Display the main menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("4. Quit")

def port_type(port):
    """Return the type of a port number."""
    if 0 <= port <= 1023:
        return "system"
    if 1024 <= port <= 49151:
        return "user"
    if 49152 <= port <= 65535:
        return "dynamic"
    return "invalid"

def check_port():
    """Ask for a port and show its type."""
    port = int(input("Port: "))
    result = port_type(port)
    border(f"Port {port}: {result}")

def password_problem(password, username):
    """Return the password problem, or '' if ok."""
    if password == username:
        return "same as the username"
    if len(password) < MIN_LENGTH:
        return "too short"
    return ""

def check_password():
    """Ask for username/password and show result."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem == "":
        border("Password accepted.")
    else:
        border(f"Rejected: {problem}")

def pin_days(digits, attempts):
    """Return days to guess a PIN."""
    total = 10 ** digits
    return total // attempts

def check_pin():
    """Ask for PIN info and show guessing time."""
    digits = int(input("PIN digits: "))
    attempts = int(input("Attempts per second: "))
    days = pin_days(digits, attempts)
    border(f"{digits} digits: {days} days")

def main():
    """Run the menu loop and count checks."""
    checks = 0
    while True:
        show_menu()
        choice = input("Choice (1, 2, 3, or q): ")
        if choice == "1":
            check_port()
            checks += 1
        elif choice == "2":
            check_password()
            checks += 1
        elif choice == "3":
            check_pin()
            checks += 1
        elif choice == "q":
            break
        else:
            border("Unknown choice.")
    border(f"Checks done: {checks}")

main()
