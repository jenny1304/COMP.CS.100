"""
COMP.CS.100 The first Python program.
Creator: Huyen Pham
"""


def main():

    feel = input("How do you feel? (1-10) ")
    num = int(feel)
    if num > 10 or num <= 0:
        print("Bad input!")
    elif num == 10:
        print("A suitable smiley would be :-D")
    elif num == 1:
        print("A suitable smiley would be :'(")
    else:
        if num > 7:
            print("A suitable smiley would be :-)")
        elif num < 4:
            print("A suitable smiley would be :-(")
        else:
            print("A suitable smiley would be :-|")




if __name__ == '__main__':
    main()