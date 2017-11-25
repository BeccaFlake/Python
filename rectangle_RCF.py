#!/usr/bin/env python3

#RECTANGLE CLASS
class Rectangle:
    #Constructor
    def __init__(self, height, width):
        self.height = height
        self.width = width

    #method that gets the perimeter
    def get_perimeter(self, height, width):
        perimeter = ((2 * width)+(2 * height))
        #return perimeter as a printable string
        return str(perimeter)

    #method that gets the area
    def get_area(self, height, width):
        area = (width * height)
        #return area as a printable string
        return str(area)
    
    #method that gets the string representation
    def str_rep(self, height, width):
        top_bottom = (" " + "* " * width)
        middle = (" *" + " " * ((width-2)*2)+ " *")
    #print the representation 
        print(top_bottom)
        #for loop that prints the central rows of the string represenation
        for i in range(height-2):
            print(middle)
        print(top_bottom)


#MAIN
def main():
#print the title
    print(" Rectangle Calculator")
    choice = "y"
    #while loop
    while choice.lower() == "y":
        #get the height input and valitdate it
        try:
            height = int(input("\n Height: "))
        except ValueError:
           height = input(" Enter the height as an integer value: ")
           continue
       # height = int(height)
        #get the width input and validate it
        try:
            width = int(input(" Width: "))
        except ValueError:
            width = input(" Enter the width as an integer value: ")
            continue
       # width = int(width)
        #create the class instance using the height and width
        rectangle = Rectangle(height, width)

        #use the perimeter method & print the result
        print(" Perimeter: " + rectangle.get_perimeter(height, width))
        #use the area method & print the result
        print(" Area: " + rectangle.get_area(height, width))
        #use the string represenation method
        rectangle.str_rep(height, width)
        #ask for the continuation input
        choice = input("\n Would you like to continue? (y/n) ")


if __name__ == "__main__":
    main()

