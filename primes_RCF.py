#!/usr/bin/env python3

#get the input and validate it
def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if (number > low) and (number < high):
            return number
        else:
            print("Invalid entry. Try again")
            print()
        
#calculate and display the factors of the input
def factors_and_prime_status(number):
    counter = 0
    for f in range(1, number+1):
        #determine and print factors
        if (number % f ==0):
            counter +=1
            print(f)                                  
    return counter    

def main():
    choice = "y"
    while choice.lower() == "y":
        print("Prime Number Checker\n")
        number = get_int("Enter a whole number between that is between 1 and 5000: ", 1, 5000)
        print("Here are the factors of your number: \n")
        counter = factors_and_prime_status(number)
     #Display the prime status and the number of factors   
        #Number is not a prime
        if counter > 2 :
            print()
            print(number, "is NOT a prime number.")
            print(number, "has", counter, "factors.")            
        #Number is a prime
        else:
            print()
            print(number, "is a prime number.")

        #ask if they would like to continue
        print()
        choice = input("Continue? (y/n): ")
        print()

    

if __name__ == "__main__":
    main()
