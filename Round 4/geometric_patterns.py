"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""
import math

def positive(question):
    """Check whether the entered dimensions are postive"""
    value = float(input(question))
    while True:
        if value <= 0:
            value = float(input(question))
        else:
            return value

def print_Results(c,a):
    """Print out the results of the calcuation"""
    print(f"The circumference is {c:.2f}")
    print(f"The surface area is {a:.2f}")

def calculate_Square(a):
    """Calculate the results required"""
    C = a*4
    A = a*a
    return C, A

def square():
    """Ask for the demensions and print final"""
    side = positive("Enter the length of the square's side: ")
    (cir, area)= calculate_Square(side)
    print_Results(cir,area)

def rectangle():
    """Ask for the demensions and print final"""
    side1 = positive("Enter the length of the rectangle's side 1: ")
    side2 = positive("Enter the length of the rectangle's side 2: ")
    C = 2*(side1+side2)
    A = side1*side2
    print_Results(C,A)

def circle():
    """Ask for the demensions and print final"""
    radius = positive("Enter the circle's radius: ")
    C = 2*math.pi*radius
    A = math.pi*radius*radius
    print_Results(C,A)

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()

        elif answer == "r":
            rectangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
