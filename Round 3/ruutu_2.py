"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""

def print_box(width, height, mark):
    """use the parameters to print  box"""
    for i in range(int(height)):
        print(mark*int(width))

def read_input(question):
    """checks whether the input is valid"""
    check = int(input(question))
    temp = True
    while temp:
        if check > 0:
            return check
        else:
            check = int(input(question))

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print("")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
