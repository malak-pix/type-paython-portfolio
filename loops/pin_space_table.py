#pin_space_table.py
#calculate time reqiered to try every possiable pin from 4 to 8 digits
GUESSES_PER_SECONED=10
for digits in range(4,9):
    combinations =10 ** digits
    seconds = combinations //GUESSES_PER_SECONED
    minutes =seconds // 60
    days = seconds// 86400
    print(f"{digits} digits :{combinations} PINs :{minutes} minutes :{days} days")