#Ask user their name
name = str(input("What is your name? "))
age = int(input("Enter your age "))
if age < 19: 
    print(name + "You are too young to drink alcohol in Ontario.")
elif age >= 19: 
    print(name +"You can drink alcohol legally in Ontario")