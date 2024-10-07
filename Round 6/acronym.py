"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""
def create_an_acronym(name):
    """ requests a name as a parameter and returns its acronym"""
    acronym = name[0]

    for i in range(0, len(name)):
        if name[i]==" ":
            acronym+=name[i+1]

    return acronym.upper()

def main():
    print(create_an_acronym("central intelligence agency"))

if __name__ == '__main__':
    main()