"""
COMP.CS.100
huyen.pham@tuni.fi
"""

def are_all_members_same(list):
    """compare uses a list as a parameter and returns information on whether all the members contained by the list are the same"""
    if len(list)==0:
        return True
    first = list[0]
    for i in range(len(list)):
        if list[i] != first:
            return False
    return True

def main():
    list = [42,42,42,42]
    print(are_all_members_same(list))

if __name__ == '__main__':
    main()