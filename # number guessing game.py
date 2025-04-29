# number guessing game 

import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please choose a number greater than zero next time!")
        quit()
else:
    print("Please type a number next time :)")
    quit()

number = random.randint(1, top_range)
guess_tracker = 0

print("I am thinking of a number between 1 and " + str(top_range) + ".")
print()

while True:
    guess_tracker += 1

    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time :)")
        continue
    
    if guess == number:
        print("You got it!")
        break
    elif guess > number:
        print("Your guess is above the number!")
    else:
        print("Your guess is below the number!")
        print("Keep trying!")
print()
print("It took you", guess_tracker, "guesses!")
print()