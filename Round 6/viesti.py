"""
COMP.CS.100 Programming 1
Code Template

Puff, the magic dragon lived by the sea,
And frolicked in the autumn mist, in a land called Honah Lee.
"""
def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13r
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    max = len(regular_chars)
    new_text=""

    for i in range(0, max):
        if text.lower() == regular_chars[i]:
            new_text = encrypted_chars[i]

    if text.islower():
        return new_text
    elif text.isupper():
        return new_text.upper()
    else:
        return text

def  row_encryption(line):
    """ perfoms a ROT13 transformation for an entire string"""
    new_line=""
    for i in range(0,len(line)):
        new_line+=encrypt(line[i])
    return new_line

def  read_message():
    """
    The function reads the input entered by the user, saves the rows in a list, and returns the list.
    :return:
    """
    list = []
    check = True
    while check:
        input_line = input("")
        if input_line == "":
            return list
        else:
           row=input_line.split("\n")
           for i in range(0,len(row)):
              list.append(row[i])

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for i in range(0,len(msg)):
        print(row_encryption(msg[i]))

if __name__ == "__main__":
    main()
