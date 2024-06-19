password_strength=""

def check(passstring):
    global password_strength
    passlen=len(passstring)
    isLower=False
    isUpper=False
    isSpecial=False
    isNumeric=False
    inputchar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(passlen):
        if passstring[i].islower():
            isLower=True
        if passstring[i].isupper():
            isUpper=True
        if passstring[i].isdigit():
            isNumeric=True
        if passstring[i] not in inputchar:
            isSpecial=True
    
    if (isLower and isUpper and isNumeric and isSpecial and passlen>=8):
        password_strength="Strong"
    elif(isLower or isUpper) and (isSpecial or isNumeric) and passlen>=6:
        password_strength="Moderate"
    else:
        password_strength="Weak"

Password=input("Enter Your Password:")

check(Password)
print("Password Strength:",password_strength)