import random

User_number = input("Enter a Number")

if User_number.isdigit():
    User_number = int(User_number)

    if User_number <= 0:
        print("Please Enter a number larger than 0 Next time.")
        quit()
else:
    print("Please Enter a Number Next time.")
    quit()

random_number = random.randint(0,User_number)
Guesses = 0
while True:
    Guesses += 1
    User_Guess_Number = input(" Make a Guess:")
    if User_Guess_Number.isdigit():
        User_Guess_Number = int(User_Guess_Number)
    else:
        print("Please Enter a Number Next time.")
        continue
    
    if User_Guess_Number == random_number:
        print("Congraulations Your's Guess is Right.")
        break
    elif User_Guess_Number > random_number:
        print(" You'r too High, Guess again.")
    else:
        print(" You'r too low, Guess again.")

print("You Get in", Guesses, "Guesses")