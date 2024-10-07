"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""
def  capitalize_initial_letters(string):
    """
    uses a string as a parameter and returns it as written, with each word starting in upper case but the rest of the world in lower case.
    :param string:
    :return:
    """
    if string!="":
        words = string.split()
        capitalized = []
        for part in words:
            capitalized.append(part.capitalize())

        result = ' '.join(capitalized)

        return result
    else:
        return ""

def main():
    capitalize_initial_letters("hello bye")
if __name__ == '__main__':
    main()