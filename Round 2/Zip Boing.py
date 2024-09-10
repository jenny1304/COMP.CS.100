"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    # max= int(input("How many numbers would you like to have? "))
    # num = 1
    # temp = True
    # while num<max+1:
    #     if num%3 == 0 and num%7 == 0:
    #         print("zip boing")
    #     elif num%3 == 0:
    #         print("zip")
    #     elif num%7 == 0:
    #         print("boing")
    #     else:
    #         print(num)
    #
    #     num += 1

    max = int(input("How many numbers would you like to have? "))
    for num in range(1, max +1):
        if num % 3 == 0 and num % 7 == 0:
            print("zip boing")
        elif num%3 == 0:
            print("zip")
        elif num%7 == 0:
            print("boing")
        else:
            print(num)



if __name__ == '__main__':
    main()