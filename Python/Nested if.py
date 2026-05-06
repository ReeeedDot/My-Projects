age= int(input("Enter your age: "))

if age >=18:
    print("you are an adult.")
    if age >=60:
        print("You are also a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")