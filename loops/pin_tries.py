#pin_tries.py
#Check PIN with a maximum of three tries
MAX_TRIES = 3
CORRECT_PIN ="2580"
tries=0
while tries<MAX_TRIES:
    pin=input("PIN: ")
    tries+=1
    the_left_tries = MAX_TRIES - tries
    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        print(f"WRONG PIN . Tries Left = {the_left_tries}")
        if tries == MAX_TRIES:
            print("Card blocked.")

