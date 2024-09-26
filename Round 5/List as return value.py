
"""
COMP.CS.100
huyen.pham@tuni.fi
"""
def input_to_list(number):
    """add the entered numbers to the list and return it"""
    list = []
    print(f"Enter {number} numbers:")
    for i in range(number):
        ans = int(input(""))
        list.append(ans)

    return list

def main():
    list = []
    count = 0
    number = int(input("How many numbers do you want to process: "))
    list = input_to_list(number)
    find = int(input("Enter the number to be searched: "))

    for i in range (number):
        if list[i] == find:
            count += 1

    if count> 0:
        print(f"{find} shows up {count} times among the numbers you have entered.")
    else:
        print(f"{find} is not among the numbers you have entered.")

if __name__ == '__main__':
    main()
