# Program: Login Decision
# Description: Checks the username, failed login attempts, and password
MAX_FAILD = 5
KNOWN_USER="analyst"
STORED_PASSWORD="Blue#Falcon72"
username=input("Username:")
faild=int(input("Faild_Attempt"))
password=input("Password:")
if faild>=MAX_FAILD:
    print("Account Locked!")
elif username !=KNOWN_USER:
    print("Unknown user")
elif password == STORED_PASSWORD:
    print("Access granted")    
else:
    attempt_left = MAX_FAILD - faild -1
    print(f"Access denied. Attempts left: {attempt_left}")

