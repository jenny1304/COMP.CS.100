"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    temp = True

    while temp:
        word = input("Bored? (y/n) ")

        if word == "Y" or word == "y":
            temp = False

        elif word == "n" or word == "N":
            temp = True

        else:
            print("Incorrect entry.")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
