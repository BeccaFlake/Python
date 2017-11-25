#!/usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print(" show -- Show the inventory.\n",
          "pick up -- Pick an item up.\n",
          "edit -- Change the name of an item in the inventory.\n",
          "drop -- Drop an item.\n",
          "exit -- Exit the program.\n")
    
def show(inventory):
    if len(inventory) == 0:
        print("The bag is empty. Well, there are a few stale crumbs.\n")
        return
    else:
        num = 1
        for item in inventory:
            print(str(num) + ". " + item)
            num += 1
        print()
        
def pick_up(inventory):
    #limit the number of items in the inventory to 4
    if len (inventory) <=3:
         new_item = input("What item would you like to add to the bag? ")
         inventory.append(new_item)
         print("The \"" + new_item + "\" was added to the bag.\n")
    else:
        print("It looks like the bag is full! You need to drop something first.\n")
    
def edit(inventory):
    #ask for the index
    num = int(input("What is the number of the item you wish to edit? "))
    #validate the input
    if num < 0 or num > len(inventory):
        print("That item does not seem to exist. Try again.\n")
    else:
        new_name = input("What would you like to change the item too? ")
        inventory[num-1] = new_name
        print("Item number " + str(num) + " has been changed to \"" + new_name + "\".\n")
        
def drop(inventory):
    #ask for the index
    num = int(input("What is the number of the item you would like to drop? "))
    #validate the input
    if num < 0 or num > len(inventory):
        print("That item does not appear to exist. Try again.\n")
    else:
        discard = inventory.pop(num-1)
        print("The item \"" + discard + "\" has been dropped.\n")

def main():
    inventory = ["A rather plain looking robe",
                 "A gnarled stick",
                 "Two pulsating gems"]
    
    print("\nWizard Inventory Program\n")
    display_menu()

    while True:
        command = input("Command: ")

        if command.lower() == "show":
            show(inventory)
        elif command.lower() == "pick up":
            pick_up(inventory)
        elif command.lower() == "edit":
            edit(inventory)
        elif command.lower() == "drop":
            drop(inventory)
        elif command.lower() == "exit":
            break
        else:
            print("That is not a valid command. Please try again.\n")
    print("Happy adventuring!")

if __name__ == "__main__":
    main()
    
