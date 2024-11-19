"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""

class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    def __init__(self, name, health):
        """
        Constructor. Initialize the name of the character and a dictionary with item name
        as key and item_amount as payload

        """
        self.__name = name
        self.__health = health
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
        print(f"Hitpoints: {self.__health}")
        if len(self.__inventory.keys()) == 0:
            print("  --nothing--")
        for item_name in sorted(self.__inventory):
            print(f"  {self.__inventory[item_name]} {item_name}")

    def remove_item(self, item_removed):
        """
        Delete the item entered as a parameter from the list
        :param item_removed: The item entered as a parameter
        """

        if self.__inventory[item_removed] == 1:
            del self.__inventory[item_removed]
        elif self.__inventory[item_removed] > 1:
            self.__inventory[item_removed] -= 1

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

    def how_many(self, item_checklist):
        """
        Return how many of one item does the character have
        """
        if item_checklist in self.__inventory:
            return self.__inventory[item_checklist]
        else:
            return 0

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """
        if item in self.__inventory:
            target.give_item(item)
            self.remove_item(item)
            return True
        else:
            return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """
        WEAPONS = {
            # Weapon          Damage
            # --------------   ------
            "elephant gun": 15,
            "gun": 5,
            "light saber": 50,
            "sword": 7,
        }

        if weapon not in WEAPONS:
            print(f'Attack fails: unknown weapon "{weapon}".')
            return
        elif weapon not in self.__inventory:
            print(f'''Attack fails: {self.__name} doesn't have "{weapon}".''')
            return
        elif self == target:
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return

        target.__health -= WEAPONS[weapon]
        print(f"{self.__name} attacks {target.__name} delivering {WEAPONS[weapon]} damage.")

        if target.__health <= 0:
            print(f"{self.__name} successfully defeats {target.__name}.")
            return

def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()

if __name__ == "__main__":
    main()
