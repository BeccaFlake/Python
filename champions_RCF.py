#!/usr/bin/env python3
FILENAME = "world_cup_champions.txt"
#Read the file in
def read_file():
    world_cups ={}
    #Break the file into tuples at each new line character
    try: 
        with open(FILENAME, "r") as file:
            for line in file:
                line.replace("'", "")
                row = line.split(",")
                world_cups[row[0]] = row[1]
        return world_cups
    except FileNotFoundError:
        print("Could not find ", FILENAME, " file.\n")
        exit()
        


def create_contents(world_cups):
    del world_cups["ï»¿Year"]
    #Separate the country names from the world cup year so that they can be consolidated
    countries= list(world_cups.values())
    years = list(world_cups.keys())
    cups=[]
    #Loop that makes a list of the country names and years, rearranged so that it is sorted by country name.
    for count in range(0, len(world_cups)):
        year = [countries[count],  years[count]]
        cups.append(year)
        count+=count
    #Alphabetize the list 
    cups.sort()

    #The lists to hold the winning years for each country.
    argentina_wins = []
    brazil_wins = []
    england_wins = []
    france_wins = []
    germany_wins = []
    italy_wins = []
    spain_wins = []
    uruguay_wins = []

    #Loop that iterates through each item in the list of world cups.
    #If the country name is in the specified index it will add the year for that world cup to the list of winning years for that country.
    count = 0
    for i in cups:
        if 'Argentina' in cups[count]:
            argentina_wins.append(int(cups[count][1]))
            count+=1
        elif 'Brazil' in cups[count]:
            brazil_wins.append(int(cups[count][1]))
            count+=1
        elif 'England' in cups[count]:
            england_wins.append(int(cups[count][1]))
            count+=1
        elif 'France' in cups[count]:
            france_wins.append(int(cups[count][1]))
            count+=1
        elif 'Germany' in cups[count]:
            germany_wins.append(int(cups[count][1]))
            count+=1
        elif 'Italy' in cups[count]:
            italy_wins.append(int(cups[count][1]))
            count+=1
        elif 'Spain' in cups[count]:
            spain_wins.append(int(cups[count][1]))
            count+=1
        elif 'Uruguay' in cups[count]:
            uruguay_wins.append(int(cups[count][1]))
            count+=1
    #The rearranged and consolidated dictionary for the world cups
    world_cups = {"Argentina": argentina_wins, "Brazil": brazil_wins,
                  "England":england_wins, "France":france_wins,
                  "Germany":germany_wins, "Italy":italy_wins,
                  "Spain":spain_wins, "Uruguay":uruguay_wins }
    return world_cups
    
#print the contents
def display(world_cups):
    #Counter for the print loop
    c = 0
    #Variables that hold the country names and winning years as printable lists
    countries = list(world_cups.keys())
    winningyears = list(world_cups.values())
    
    print("{:17} {:5} {:5}".format(" Country", "Wins", "Years"))
    print("{:17} {:5} {:5}".format(" =======", "====","====="))
    #A while loop that prints each dictionary entry, as well as the number of wins for that country.
    while c < len(countries):
        country = str(countries[c])
        wins= str(len(winningyears[c]))
        years = str(winningyears[c])
        print("", country.ljust(16), wins.ljust(5), years.strip("[]"))
        c +=1

def determine_winner(world_cups):
    #Variables that hold the country names and winning years as lists
    countries = list(world_cups.keys())
    winningyears = list(world_cups.values())
    #Counter and variable to hold the index of the country with the most wins
    c = 0
    mostwins = 0
    #Compare the lengths of the items in the winning years list
    for i in range(len(winningyears[c+1])):
        if len(winningyears[c]) > len(winningyears[c+1]):
            mostwins = c
            c+=1  
        else:
            c+=1  
    print("\n The country with the most wins is: ", countries[mostwins]) 
    
def main():
    print(" FIFA World Cup Winners\n")
    choice = "n"
    while choice.lower() == 'n':
        world_cups = read_file()
        world_cups = create_contents(world_cups)
        display(world_cups)
        determine_winner(world_cups)
        choice = input("\n Exit? (y/n) ")

if __name__ == "__main__":
    main()

