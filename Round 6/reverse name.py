"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""
def reverse_name(string_name):
    """ changes name to the order where the first name is followed with the last name."""

    if "," in string_name:
        name_separated = string_name.strip().split(",")
        if name_separated[0]=="" and name_separated[1]=="":
            return ""
        elif name_separated[0]=="":
            return name_separated[1].strip()
        elif name_separated[1]=="":
            return name_separated[0].strip()
        else:
            return f"{name_separated[1].strip()} {name_separated[0].strip()}"
    else:
        if " " in string_name:
            name_separated = string_name.strip().split(" ")
            return f"{name_separated[0].strip()} {name_separated[1].strip()}"
        else:
            return string_name
def main():
    print(reverse_name(' , Y '))

if __name__ == '__main__':
    main()