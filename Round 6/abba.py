"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""

def count_abbas(string):
    """returns the number of abbas (meaning the string "abba") that the parameter string contains."""
    count = 0
    for i in range(0,len(string)-3):
        if string[i:i+4]== 'abba':
            count +=1

    return count


    return count
def main():
    print(count_abbas("abbabbabba"))
if __name__ == '__main__':
    main()