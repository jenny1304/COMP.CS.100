"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    number =  int(input("Choose a number: "))
    count = 1

    while count<11:
        ans = count * number
        print(count, "*", number, "=", ans)
        count += 1

if __name__ == '__main__':
    main()