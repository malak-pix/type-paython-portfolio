# fix_the_session.py
# This program reports a user's session time.
   
username = input("Username: ")
#the total_seconds is str we should convert it to int  run time error
total_seconds = int(input("Session length in seconds: "))
#we should put double slash to get int num whitout frictional part
minutes = total_seconds // 60 
seconds = total_seconds % 60
  
print("=" * 30)
#forget f
print(f"User: {username}")
#the + connector only for strings and here we have int
print(f"Session:   {minutes}   min   {seconds} s")
#we forget a parenthes
print("=" * 30)