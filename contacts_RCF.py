#!/usr/bin/env python3

#import the csv library and define the file to be used
import csv
FILENAME = "contacts.csv"

#function that writes to the file 
def write_contacts(contacts):
    with open (FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

#function that reads from the file
def read_contacts():
    contacts = []
    with open (FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

#function that lists the contact names in a numbered list
def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])                     #The number assigned to each contact is the index + 1.
    print()    

#function that prints the information of a specified contact
def view_contact(contacts):
    number = int(input("What is the number of the contact you wish to view? "))     
    index = number - 1
    #validate the input and then print the contents of specified row
    if index >= 0 and index <= (len(contacts)-1):
        contact = contacts[index]
        print("Name: " + contact[0])
        print("E-mail: " + contact[1])
        print("Phone: " + contact[2])
        print()
    else:
        print("That is not a valid entry. Please try again.\n")
    
#function that adds a new entry to the file
def add_contact(contacts):
    #get the entry
    name = input("Name: ")
    email = input("E-mail: ")
    phone = str(input("Phone: "))
    #write the entry to the file
    contact = []
    contact.append(str(name))
    contact.append(str(email))
    contact.append(str(phone))
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

#function that removes an entry from the file
def delete_contact(contacts):
    number = int(input("What is the number of the contact you wish to delete? "))
    index = number - 1
    #Validate the input and then pop the specified contact out of the file
    if index >= 0 and index <= (len(contacts)-1):
        contact = contacts.pop(index)
        write_contacts(contacts)
        print(contact[0] + " was removed.\n")
    else:
        print("That is not a valid entry. Please try again.\n")

#function that prints the list of commands to the console
def display_menu():
    print("COMMAND LIST")
    print("list -- print list of contacts\n"
          "view -- print the information for a single contact\n"
          "add -- add a new contact to the file\n"
          "del -- remove a contact from the file\n"
          "exit -- exit the program\n")
    
def main():
    print("Contact Manager\n")
    display_menu()
    #assign contacts variable to the read_contact() function
    contacts = read_contacts()
    while True:
        command = input("Enter a command: ")
        #if statements that use the commands to call the functions
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
            print("That is not a valid command. Please try again\n.")
    print("Goodbye.")
    
if __name__ == "__main__":
    main()
    
