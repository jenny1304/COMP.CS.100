"""
COMP.CS.100
huyen.pham@tuni.fi
"""

def  is_the_list_in_order(list):
    """compare uses a list as a parameter and returns information on whether all the members contained by the list are the same"""
    count = 0
    if len(list)==0 or len(list)==1:
        return True
    first = list[0]
    for i in range(1,len(list)):
        if first <= list[i]:
            count +=1
            first = list[i]

    if count == len(list)-1:
        return True
    else:
        return False

def main():
    list = [42,41,44,45]
    print(is_the_list_in_order(list))

if __name__ == '__main__':
    main()