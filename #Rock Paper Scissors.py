#Rock Paper Scissors

#imports random module.
import random

#varibles used in code.
user_wins = 0
computer_wins = 0 
tie_counter = 0
options = ["rock", "paper", "scissors"]
user_name = input("What is your name? ")

#Game Starts Here 
while True:
   #Setting up code for user input.
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
    
    #Allows users to press "q" to exit the game and break the while-loop.
    if user_input == "q":
        break

    #Checks if user input is valid (e.g. Rock, Paper, or Scissor)    
    if user_input not in options:
        print ("Try again.")
        continue
    
    #Computer genertates a random number then that number is used to check the "options" list with that number.
    random_number = random.randint(0,2)
    #Rock: 0, Paper: 1, Scissors: 2
    computer_choice = options [random_number]
    print ("Computer picked,", computer_choice + ".")

    #Checks for win conditions x3 Adds one to user wins varible.
    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    
    #Checks for tie condition by checking if user and computer choices are the same. Adds one to tie varible.
    elif user_input == computer_choice:
        print("You tied!")
        tie_counter =+ 1
    
    #if none of the above win conditions are met, users loses and adds one to computer wins.
    else: print("You Lost!")
    computer_wins += 1
    #while-loop restarts.
    continue

#After user quits, scoreboard is displayed. tie_counter is converted to a string to allow it to be displayed with print.
print()
print(user_name + ":", user_wins, "wins.")
print("Computer:", computer_wins, "wins.") 
print("Ties:", str(tie_counter) + ".")
print()
print("Goodbye! Thanks for playing!")

