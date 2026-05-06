ch=(input("Enter a single character: "))
if ch in['a','e','i','o','u']:
    print(f"{ch} is a Vowel")
elif ch.isalpha():
    print(f"{ch} is a consonant")
else:
    print("Invalid input! Please Enter alphabet character.")