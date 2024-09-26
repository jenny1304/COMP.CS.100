"""
COMP.CS.100
huyen.pham@tuni.fi
"""

def find_time(number):
    """Find the next 3 time stamps
     if reaches the end oof the list, the starting index would be renewed"""
    fixed_time = [630, 1015, 1415, 1620, 1720, 2000]
    for i in range(0, len(fixed_time)):
        if number >= 2000:
            start=0
            break
        if fixed_time[i]>=number:
            start = i
            break

    count = 3
    while count > 0:
        print(fixed_time[start])
        start += 1
        count -= 1
        if fixed_time[start-1]>=2000 :
            start = 0

def main():
    time = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    find_time(time)
if __name__ == '__main__':
    main()