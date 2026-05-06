fixed_number = 7
while  True:
    guess= int(input("Guess the Number: "))
    if guess == fixed_number:
        print("\U0001F389 Correct! You guessed it!")
        break
    else:
        print("wrong guess, try again...")