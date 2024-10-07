"""
COMP.CS.100 Programming 1
ROT13 program code template
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
