import random

#Program Introduction
print("Welcome to Our Password Generator!")

#Set Password Length
pwd_length = int(input("Enter the length of the password: "))

#Password Criteria
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pwd_symbols = lowercase.copy()

has_upper = input("Include uppercase characters? (y/n): ")
if has_upper == "y" or has_upper == "Y": 
    pwd_symbols.extend(uppercase)
#pwd_symbols = pwd_symbols + uppercase

has_special = input("Include special characters? (y/n): ")
if has_special == "y" or has_special == "Y": 
    pwd_symbols.extend(special)
#pwd_symbols = pwd_symbols + uppercase

has_digits = input("Include digits? (y/n): ")
if has_digits == "y" or has_digits == "Y": 
    pwd_symbols.extend(digits)
#pwd_symbols = pwd_symbols + uppercase

new_password = "" #Empty string to hold new password

while len(new_password) != pwd_length:
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol
    #end of while loop

print(f"{new_password} Has been generated")
