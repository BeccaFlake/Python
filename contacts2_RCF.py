#!/usr/bin/env python3

#import the csv library and define the file to be used
import csv
FILENAME = "contacts.csv"

#Function that writes to the file 
def write_contacts(contacts):
    with open (FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)     

#Function that reads from the file
def read_contacts():
    contacts = []
    try:
        with open (FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    #If the file cannot be found, opens a new CSV 
    except FileNotFoundError:
        print("Could not find the contacts file!\n"
              "Starting a new contacts file... \n")
        return contacts        
            
#Function that lists the contact names in a numbered list
def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        #The number assigned to each contact is the index + 1.
        print(str(i+1) + ". " + contact[0]) 
    #Inform the user if the file is empty
    if (len(contacts) == 0):
        print("There are no contacts in the list")
    print()
    

#Function that prints the information of a specified contact
def view_contact(contacts):
    while True:
        #Inform the user if the file is empty and stop the loop
        if (len(contacts) == 0):
            print("There are no contacts in the list.\n")
            return False
        #Proceed if the file is not empty, checking for valid input
        try:
            index = int(input("What is the number of the contact you wish to view? "))-1
        except ValueError:
            print("Invalid integer. Please try again.\n")
            continue
        if index < 0 or index > (len(contacts)-1):
            print("Invalid contact number. Please try again.\n")   
        else:
            break
    contact = contacts[index]
    print("Name:   " + contact[0])
    print("E-mail: " + contact[1])
    print("Phone:  " + contact[2])
    print()

    
#Function that adds a new entry to the file
def add_contact(contacts):
    #get the entry
    name = input("Name: ")
    email = input("E-mail: ")
    phone = str(input("Phone:"))
    #write the entry to the file
    contact = []
    contact.append(str(name))
    contact.append(str(email))
    contact.append(str(phone))
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

#Function that removes an entry from the file
def delete_contact(contacts):
        while True:
            #Inform the user if the file is empty and stop the loop
            if (len(contacts) == 0):
                print("There are no contacts in the list.\n")
                return False
            #Proceed if the file is not empty, checking for valid input
            try:
                index = int(input("What is the number of the contact you wish to delete? "))-1
            except ValueError:
                print("Invalid integer. Please try again.\n")
                continue
            if index < 0 or index > (len(contacts)-1):
                print("Invalid contact number. Please try again.\n")
            else:
                break
        contact = contacts.pop(index)
        write_contacts(contacts)
        print(contact[0] + " was removed.\n")
       

#Function that prints the list of commands to the console
def display_menu():
    print("COMMAND LIST\n"
          "list -- print list of contacts\n"
          "view -- print the information for a single contact\n"
          "add  -- add a new contact to the file\n"
          "del  -- remove a contact from the file\n"
          "exit -- exit the program\n")
    
def main():
    #Assign contacts variable to the read_contact() function
    contacts = read_contacts()
    print("Contact Manager\n")
    display_menu()
    while True:
        command = input("Enter a command: ")
        #If statements that use the commands to call the functions
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "view":
            view_contact(contacts)
        elif command.lower() == "add":
            add_contact(contacts)
        elif command.lower() == "del":
            delete_contact(contacts)
        elif command.lower() == "exit":
            break
        #input validation
        else:
            print("That is not a valid command. Please try again.\n")
    print("Goodbye.")
    
if __name__ == "__main__":
    main()
    
