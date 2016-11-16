# Phyllis Torres
# Module 13: Inheritance
# Due 12/2/2016

# This program will call the officeFurniture module to use for the class definitions

# import the Office Furniture class
import officeFurniture

def main():
    # creating an object of the Furniture
    cabinet = officeFurniture.Furniture("File Cabinet", "Wood", 15, 16, 24, 3, 75.50)

    # printing the information
    print("Product: " + cabinet.get_category())
    print("Material: " + cabinet.get_material())
    print("Length: " + str(cabinet.get_length()))
    print("Width: " + str(cabinet.get_width()))
    print("Height: " + str(cabinet.get_height()))
    print("Quantity: " + str(cabinet.get_quantity()))
    print("Price: ${:0,.2f}\n".format(cabinet.get_price()))

    print cabinet

# call the function

main()
