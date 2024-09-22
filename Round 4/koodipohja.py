"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
"""

def print_box(width, height, border_mark="#",inner_mark=" " ):
    """Print a box according to input values and use 2 different marks"""
    print(border_mark*width)
    for i in range (height-2):
        print(f"{border_mark}{inner_mark*(width-2)}{border_mark}")
    print(border_mark * width)

def main():
    print_box(5, 4)
    print("")
    print_box(3, 8, "*")
    print("")
    print_box(5, 4, "O", "o")
    print("")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()
