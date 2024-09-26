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
    print("The numbers you entered that were greater than zero were:")
    for k in range(5):
        if list[k]>0:
            print( list[k])


if __name__ == '__main__':
    main()