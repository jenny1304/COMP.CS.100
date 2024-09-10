"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():

    temp= True


    while temp:
        word = input("Answer Y or N: ")

        if word == "Y" or word == "N" or word == "y" or word == "n":
            temp = False

        else:
            print("Incorrect entry.")

    if word == "Y":
        print("You answered Y")
    elif word == "y":
        print("You answered y")
    elif word == "N":
        print("You answered N")
    elif word == "n":
        print("You answered n")

if __name__ == '__main__':
    main()