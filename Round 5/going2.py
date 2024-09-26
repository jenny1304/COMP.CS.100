"""
COMP.CS.100
huyen.pham@tuni.fi
"""

def main():
    list = []
    print("Give 5 numbers:")
    for i in range(5):
        number = int(input("Next number: "))
        list.append(number)
    print("The numbers you entered, in reverse order:")
    for k in range(4,-1,-1):
        print( list[k])


if __name__ == '__main__':
    main()