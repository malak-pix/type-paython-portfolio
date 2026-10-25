#Login Rik Score
#calculate a login risk score based on faild attempt
score = 0
faild=int(input("Faild Attempt in the last hour:"))
hour =int(input("Login hour (0-23):"))
new_device =input("New device (yes/no):")
if faild >=3:
    score += 40
if hour <6:
    score+=30
if new_device == "yes":
    score+=30

if score >= 70:
    level="HIGH"
elif score >= 30:
    level ="MEDIUM"
else:
    level ="LOW"
print(f"Risk Score:{score}({level})")        
