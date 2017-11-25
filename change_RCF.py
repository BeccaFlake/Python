#!/usr/bin/env python3
#This program calculates  the coins needed to make change for a specified monetary amount


#Display Title
print("Change Calculator\n\n")
    
#initialize the variables
qcounter = 0
dcounter = 0
ncounter = 0
pcounter = 0

quarters = 0
dimes = 0
nickels = 0
pennies = 0

choice = "y"
while choice.lower() == "y":
    
    #Ask for the input
    dollar_amount = float(input("Enter the dollar amount. (For example 3.75, 4.00, or 0.36): "))
    change = int(dollar_amount * 100)    #Multiply by 100 to convert the input to a intiger without losing the decimal portion
    
    #Calculate 
    while change > 0:
        if change >= 25:                #count needed quarters
            change -= 25
            qcounter += 1
            quarters = qcounter     
        elif change >= 10:              #count needed dimes
            change -= 10
            dcounter +=1
            dimes = dcounter
        elif change >= 5:               #count needed nickels
            change -= 5
            ncounter +=1
            nickels = ncounter
        else:                           #count needed pennies
            change -= 1
            pcounter += 1
            pennies = pcounter
        continue
                     
    #Display the result
    print("Quarters: " + str(quarters))
    print("Dimes: " + str(dimes))
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(pennies))
    print()
          
    #Ask if the user wants to continue (y/n). Continue only if user enters a y or a Y.
    choice = input("Continue? (y/n): ")
    print()
    if input == "y" or "Y":             #resets all of the calculation variables to zero when the program goes through another loop
        qcounter = 0
        dcounter = 0
        ncounter = 0
        pcounter = 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        
#Print message if user does not choose to continue                              
print("Bye!")
