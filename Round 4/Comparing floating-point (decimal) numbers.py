"""
COMP.CS.100
huyen.pham@tuni.fi
"""
import math

def compare_floats(num1,num2,EPSILON):
    """Used to check the epilson something from 2 numbers """
    return abs(num1-num2)<EPSILON

def main():
    number1= float(input("Enter 1st number: "))
    number2 = float(input("Enter 2nd number: "))
    epi = float(input("Enter epsilon: "))
    ans = compare_floats(number1,number2,epi)
    print(ans)
if __name__ == '__main__':
    main()