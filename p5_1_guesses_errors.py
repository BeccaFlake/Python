#!/usr/bin/env python3

"""
Project Statement
The guessing game has four errors. Find and correct the errors so that
the user can set an upper limit to the range of numbers, it gets a random
number in that range, and allows the user to guess until correct. It should
display 'too high' or 'too low' hints.
-------------------------------------------------------------------------
When you fix the program, upload the working program and list, as comments,
the errors you found and fixed.
Error 1: Call to the limit function in the main function did not pass the limit argument into the function. 
Error 2: Count was not initailized before being used in the function
Error 3: The second elif clause used >= instead of >, which made the program print "too high" when the answer was correct
Error 4: Count was not being passed into the print fuction with a value more than 0, which was fixed by initializing count outside of the while loop.
I also had the counter add one for a correct guess since that made more sense to me.
(Main function also did not have a colon)
"""

import random

def display_title():
    print("Guess the number!")
    print()

def set_limit():
    print("Enter the upper limit for the range of numbers: ")
    limit = int(input())
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    count = 0
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            count += 1
            print("You guessed it in " + str(count) + " tries.\n")
            return
        
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = set_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

