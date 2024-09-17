"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""

def repeat_name(name, times):
    """reapeat the names with the amount of times required"""
    if times == 3:
        print(f"{name}, {name} Bear")
        print(f"{name}, {name} Bear")
        print(f"{name}, {name} Bear")
    if times == 1:
        print(f"{name}, {name} Bear" * times)


def verse(verse,name):
    """print the verse while calling the repeat_name function"""
    print(verse)
    print(f"{name}, {name}")
    print(verse)
    repeat_name(name, 3)
    print(verse)
    repeat_name(name, 1)

def main():
    verse("I know someone you don't know","Yogi")
    print("")
    verse("Yogi has a best friend too", "Boo Boo")
    print("")
    verse("Yogi has a sweet girlfriend", "Cindy")
if __name__ == '__main__':
    main()