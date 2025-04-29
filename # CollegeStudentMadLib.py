# College Student MadLib

print("Welcome to the College Student Mad Lib Generator!")

# Input prompts
adjective1 = input("Enter an adjective: ")
class_subject1 = input("Enter a class subject: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
class_subject2 = input("Enter a class subject: ")
emotion = input("Enter an emotion: ")
name = input("Enter a name: ")
campus_location = input("Enter a campus location: ")
food_item = input("Enter a food item: ")
verb_ing = input("Enter a verb ending in -ing: ")
noun3 = input("Enter another noun: ")
adjective2 = input("Enter another adjective: ")
school_task = input("Enter a school related task: ")

# Mad Lib Output
print()
print("Here is your completed Mad Lib!")

print("""
It was a %s morning when I woke up late for my %s class. 
I grabbed my %s and ran out the door, almost forgetting my %s. 
On the way to campus, I bumped into my %s professor, who gave me a %s look.

After class, I met up with my friend %s at the %s to grab some %s. 
We spent the afternoon %s instead of studying for our big %s exam.

By the end of the day, I was completely %s but still managed to finish my %s before midnight.
"""
%(adjective1, class_subject1, noun1, noun2, class_subject2, emotion, name, campus_location, food_item, verb_ing, noun3, adjective2, school_task))

# Bonus points if you took an animal with you to school. 