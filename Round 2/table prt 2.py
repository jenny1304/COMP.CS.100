"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    number =  int(input("Choose a number: "))
    count = 1
    temp = True

    while temp:
        ans = count * number
        print(count, "*", number, "=", ans)
        count += 1

        if ans >100:
           temp = False

if __name__ == '__main__':
    main()