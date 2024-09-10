def main():

    p1= input("Player 1, enter your choice (R/P/S): ")
    p2= input("Player 2, enter your choice (R/P/S): ")

    if p1 in ("P") and p2 in ("S") or p1 in ("S") and p2 in ("R") or p1 in ("R") and p2 in ("P"):
        print("Player 2 won!")

    elif p1 in ("P") and p2 in ("R") or p1 in ("S") and p2 in ("P") or p1 in ("R") and p2 in ("S"):
        print("Player 1 won!")

    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()