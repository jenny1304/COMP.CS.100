def main():
    age = input("Please, enter your age: ")

    a = int (age)

    if a > 24:
        ticket_price = 2.04
    elif a>=17 and  a<= 24:
        ticket_price = 1.47
    elif a>=7 and  a<= 16:
        ticket_price = 01.02
    elif a>=0 and  a<= 6:
        ticket_price = 0.00

    print("Your ride will cost:", ticket_price)


if __name__ == "__main__":
    main()