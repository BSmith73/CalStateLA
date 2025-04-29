# Quiz Game
print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's play!")

score = 0

answer = input('What does ID stand for? ').lower()
print()
if answer == "instructional design":
    print('Correct! Well done!')
    score += 1
else: print('Sorry, that\'s not right.')
print()
answer = input('What does ISD stand for? ').lower()
print()
if answer == "instructional systems design":
    print('Correct! Well done!')
    score += 1
else: print('Sorry, that\'s not right.')
print()
answer = input('What is the first step in ADDIE? ').lower()
print()
if answer == "analyze":
    print('Correct! Well done!')
    score += 1
else: print('Sorry, that\'s not right.')
print()
answer = input('What is the last step in ADDIE? ').lower()
print()
if answer == "evaluate":
    print('Correct! Well done!')
    score += 1
else: print('Sorry, that\'s not right.')
print()

print('Thanks for playing! Your score was ' + str(score) + ' out of 4.')
print("You got " + str((score/4) * 100) + "%.")

