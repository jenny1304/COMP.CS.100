"""
COMP.CS.100 Programming 1
"""

def main():
    name = input("Enter the name of the file: ")
    try:
        text_file = open(name, mode="w")
    except OSError:
        print(f"Writing the file {name} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    index = 1
    while True:
        text = input()
        if text == "":
            break
        text_line = f"{index} {text}"
        print(text_line, file=text_file)
        index += 1

    text_file.close()
    print(f"File {name} has been written.")

if __name__ == '__main__':
    main()