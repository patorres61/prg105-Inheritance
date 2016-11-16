# Phyllis Torres
# Module 13: Inheritance
# Due 12/2/2016

# This program will call the officeFurniture module to use for the class definitions

# import the Office Furniture class
import officeFurniture

def main():
    # creating an object of the Furniture sub class for Desk
    desk = officeFurniture.Desk("Desk", "Metal", 48, 20, 36, 2, "Left", 3, 155.50)

    # printing the information
    print("Product: " + desk.get_category())
    print("Material: " + desk.get_material())
    print("Length: " + str(desk.get_length()))
    print("Width: " + str(desk.get_width()))
    print("Height: " + str(desk.get_height()))
    print("Number of Drawers: " + str(desk.get_drawers()))
    print("Location of Drawers: " + desk.get_location())
    print("Quantity: " + str(desk.get_quantity()))
    print("Price: ${:0,.2f}\n".format(desk.get_price()))

    print desk

# call the function

main()
