"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    def __init__(self, name):
        """
        Constructor. Initialize the name of the character and a dictionary with item name
        as key and item_amount as payload

        """
        self.__name = name
        self.__inventory = {}

    def give_item(self, added_items):
        """
        :param added_items: The items added to the character inventory
        """
        if added_items not in self.__inventory:
            self.__inventory[added_items] = 0

        self.__inventory[added_items] += 1

    def printout(self):
        """Print out the inventory and the amount of items"""
        print(f"Name: {self.__name}")
        if len(self.__inventory.keys()) == 0 :
            print("  --nothing--")
        for item_name in sorted(self.__inventory):
            print(f"  {self.__inventory[item_name]} {item_name}")

    def remove_item(self, item_removed):
        """
        Delete the item entered as a parameter from the list
        :param item_removed: The item entered as a parameter
        """

        if self.__inventory[item_removed]==1:
            del self.__inventory[item_removed]
        elif self.__inventory[item_removed]>1:
            self.__inventory[item_removed]-=1

    def get_name(self):
        """
        Return the name of the object that called this method
        :return: Name of character
        """
        return self.__name

    def has_item(self, item_checklist):
        """
        Check whether the character has a certain item or not
        :param item_checklist: The item in the list that will
        be used to check if character has that item
        """
        if item_checklist in self.__inventory:
            return True
        else:
            return False

    def how_many(self,item_checklist):
        """
        Return how many of one item does the character have
        """
        if item_checklist in self.__inventory:
            return self.__inventory[item_checklist]
        else:
            return 0

def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")



if __name__ == "__main__":
    main()
