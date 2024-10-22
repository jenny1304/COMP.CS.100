"""
COMP.CS.100 Programming 1
"""

def main():
    name_file = input("Enter the name of the file: ")
    try:
        file = open(name_file, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    index = 1
    for line in file:
        line = line.rstrip()
        print(f"{index} {line} ")
        index += 1

if __name__ == '__main__':
    main()