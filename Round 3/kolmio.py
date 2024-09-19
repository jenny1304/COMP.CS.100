"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(a,b,c):
    """calculate the area of triangle using the 3 sides"""
    s = (float(a) + float(b)+ float(c))/2
    A = sqrt(s*(s-float(a))*(s-float(b))*(s-float(c)))
    return A

def main():
    side1 = input("Enter the length of the first side: ")
    side2 = input("Enter the length of the second side: ")
    side3 = input("Enter the length of the third side: ")
    ans = area(side1,side2,side3)
    print(f"The triangle's area is {ans:.1f}")


if __name__ == "__main__":
    main()
