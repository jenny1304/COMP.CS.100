"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    day = 3
    dayMonth= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range (1, 13):

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            max = 31
        elif month == 2:
            max = 28
        else:
            max = 30


        for day in range (day, max + 1, 7):
            print(f"{day}.{month}.")
        # Check if the day exceeds the days in that month
        # => calculate the first friday of next month
        # (thang 2) 28+7-28 = 7 => correct
        day = day + 7 - dayMonth[month -1]



if __name__ == '__main__':
    main()