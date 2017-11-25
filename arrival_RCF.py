#!/usr/bin/env python3
from datetime import datetime, time, date, timedelta

import locale

def get_date():
    while True:
        date = input("\nPlease enter the estimated departure date (YYYY-MM-DD): ")
    #validate
        try:
            departure_date = datetime.strptime(date, "%Y-%m-%d")
            return departure_date
        except ValueError:
            print("Invalid format. Please try again.\n")
            continue

    
def get_time():
    while True:
        time = input("Please enter the estimated time of departure(HH:MM AM/PM): ")
        try:
            departure_time = datetime.strptime(time, "%I:%M %p")
            return departure_time
        except ValueError:
            print("Invalid format. Please try again.\n")
            continue           
    
def get_dist():
    while True:
        miles = input("Enter miles to be travelled: ")
    #validate
        try:
            miles = int(miles)
            if miles <= 0:
                print("Invalid entry. Please enter a number greater than zero.\n")
            else:
                return miles
        except ValueError:
            print("Invalid format. Please Try again\n")
            continue
    
def get_speed():
   while True:
        speed = input("Enter miles per hour: ")
    #validate
        try:
            mph = int(speed)
            if mph <= 0:
                print("Invalid entry. Please enter a number greater than zero.\n")
            else:
                return mph
        except ValueError:
            print("Invalid format. Please Try again\n")
            continue

def calculate(departure_date, departure_time, miles, mph):
    #calculate travel time
    hours = int(miles/mph)
    minutes = int(((miles/mph)-hours)*60)
    travel_time = timedelta(hours=hours, minutes=minutes)


    #estimate the date and time of arrival
    #Handle the possibility  of the trip spanning multiple days
    midnight = datetime.strptime("12:00 AM", "%I:%M %p")
    time_to_midnight = (midnight - departure_time) + timedelta(days=1)  #a variable that holds the hours and minutes between the departure date and midnight
    elapsed_time = travel_time                                          #a copy of the travel time that can be modified
    if elapsed_time >= time_to_midnight:
        elapsed_time += timedelta(days = 1)
      
    print("\n\nEstimated Travel Time")
    print("Hours: ", hours)
    print("Minutes: ", minutes)
    arrival_date = departure_date + elapsed_time 
    print("Estimated Date of Arrival: ", arrival_date.strftime("%Y-%m-%d"))
    arrival_time = departure_time + travel_time
    print("Estimated Time of Arrival: ", arrival_time.strftime("%I:%M %p"))    
    
def main():
    print("Arrival Time Estimator")
    choice = "y"
    while choice.lower() == "y":
        #call functions
        departure_date = get_date()
        departure_time = get_time()
        miles = get_dist()
        mph = get_speed()
        calculate(departure_date, departure_time, miles, mph)
        choice = input("Continue? (y/n): ")
    print("bye!")

if __name__ == "__main__":
    main()
