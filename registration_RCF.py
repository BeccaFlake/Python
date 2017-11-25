#!/usr/bin/env python3

#This program will allow a student to complete a registrationform
#The program output is a completion message that includes the user's full name and a temporary password

#Display a prompt asking for the student's full name and birth year
print("Welcome to Registration \n\n")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name:  ")
birth_year = input("Please enter your birth year: ")

#Compile the name into a single string
full_name = first_name + " " + last_name

#Generate the password by combining the first name, an asterisk, and the birth year
password = first_name + "*" + birth_year

#Print the information on three lines
print("\n")
print("Welcome, " + full_name + "!")     
print("You have successfully completed registration.") 
print("Your temporary password is: " + password)
input('Press ENTER to exit')

