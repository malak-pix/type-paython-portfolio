# fix_the_rules.py
# This program checks a connection against three rules.
role = input("Role: ")
#we add int() fun to got the right output
port = int(input("Port: "))
#we assignment role = "admin" but we want to check 
#is_admin = role = "admin" semantic
is_admin = role == "admin"
#the right way to write =< is <=
#is_system_port = port =< 1023 syntax
is_system_port = port <= 1023
#we put 443 with or so always it will give us true semantic
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
