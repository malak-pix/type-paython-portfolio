#Login Report
#Report faild login attempt and attempts remainig
MAX_LOGIN_ATTEMPT = 5
username=input("enter your username:")
faild=int(input("faild attempt:"))
attempt_remainig = MAX_LOGIN_ATTEMPT - faild
print('='*30)
print("LOGIN REPORT")
print('='*30)
print(f"User:\t{username}")
print(f"faild:\t{faild}")
print(f"left:\t{attempt_remainig}")
