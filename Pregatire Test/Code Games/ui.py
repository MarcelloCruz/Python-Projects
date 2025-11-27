
from functions import *


def menu_start():
    print("Welcome to Digit Scribble")
    number = str(generate_number())
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess == 8086:
                print(f"The number is {number}")
                continue

            if 1000 <= guess <= 9999:
                runner , reporter = checkn(number, str(guess))

                if reporter == 4:
                    print("You win!")
                    break

                else:
                    print(f"Reporters: {reporter} | Runners: {runner}")
            else:
                print(f"Please enter a number between 1000 and 9999")

        except ValueError:
            print("Please enter a number between 1000 and 9999")