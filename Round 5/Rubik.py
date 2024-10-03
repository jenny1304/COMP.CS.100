"""
COMP.CS.100
huyen.pham@tuni.fi

"""

def sort_calcualte(list):
    """Calcualte the average after sorting list from small to large and removing fastest and longest time"""
    sort_l = sorted(list)
    del sort_l[(len(sort_l)-1)]
    del sort_l[0]
    sum= 0
    for i in range(0,3):
        sum = sort_l[i] + sum

    average = sum / len(sort_l)

    return average

def main():
    time = []
    for i in range(5):
        number = float(input(f"Enter the time for performance {i+1}: "))
        time.append(number)

    ans = sort_calcualte(time)
    print(f"The official competition score is {ans:.2f} seconds.")


if __name__ == '__main__':
    main()