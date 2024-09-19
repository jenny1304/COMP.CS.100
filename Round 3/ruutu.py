"""
COMP.CS.100 Programming 1
Template for task: box printing
"""
def print_box(width, height, mark):
    """use the parameters to print  box"""
    for i in range(int(height)):
        print(mark*int(width))

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
