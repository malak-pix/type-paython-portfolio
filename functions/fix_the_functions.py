# fix_the_functions.py
#name error'print header()' is not defined
 
 
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30
          )
def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        return total #it was return zero this is not correct
    return 0
 
 
def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


print_header()
print(login_line(usernmae="sara", failed=4))#username not user
print (login_line("omar", 1))