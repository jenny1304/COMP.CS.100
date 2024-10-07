"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""

def longest_substring_in_order(string):
    """ takes a string as its parameter and searches for the longest substring with its characters in alphabetic order"""
    if len(string)<=1:
        return string

    current = longest = string[0]

    for i in range(1,len(string)):
        if string[i]>=string[i-1]:
            current += string[i]
        else:
            if len(current)>len(longest):
                longest = current
            current = string[i]


    if len(current) > len(longest):
        longest = current

    if len(set(string)) == 1:  # If all characters are the same
        return text[0]

    return longest

def main():
    print(longest_substring_in_order('abcdefghijklmefghijklmnopopqefgabcde'))
if __name__ == '__main__':
    main()