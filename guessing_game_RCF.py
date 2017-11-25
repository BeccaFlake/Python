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

Error 1: The main() function definition did not have a colon. This prevented
the program from running at all. The addition of a colon to the definition
allowed the program to run.

Error 2: The call to the play_game() function did not pass the limit variable
into the play_game() function. The function had no argument to work with and
would not execute. Inserting the limit variable as the argument
in both the function call and definition fixed this error. The example also
seemed to use the limit itself as a possible value, so I added one to the limit
argument in the random() function to allow for this. 

Error 3: Count was not initialized before being used in the play_game()
function. Setting the count variable to zero outside of the while loop
debugged this error. I also had the counter add one for a correct guess
which is what the example seemed to do.

Error 4: The first elif clause used greater than or equal to (>=) for the
relational operator. This made the program print "too high" when the answer
was too high AND when it was correct. Replacing it with just a greater than
relational operator (>) fixed this error.
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
    number = random.randint(1, limit+1)
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

