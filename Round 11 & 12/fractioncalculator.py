"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""
class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def __str__(self):
        """a fraction could be printed just like other datatypes: print(frac)."""
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


    def simplify(self):
        """Simplify the fraction and return new numerator and denominator"""
        divisor = greatest_common_divisor(self.__numerator,self.__denominator)
        numerator = self.__numerator//divisor
        denominator=self.__denominator//divisor
        new = Fraction(numerator, denominator)
        return new

    def complement(self):
        """modifying the object that the method is called for"""
        numerator = 0-self.__numerator
        new_frac = Fraction(numerator,self.__denominator)
        return new_frac

    def reciprocal(self):
        """Return the reciprocal"""
        numer = self.__denominator
        deno =self.__numerator
        new_frac = Fraction(numer,deno)
        return new_frac

    def multiply(self, frac2):
        """Multiplyy the 2 fractions"""
        numerator= self.__numerator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        new = Fraction(numerator,denominator)
        return new

    def divide(self,frac2):
        """Divide the 2 fractions"""
        numerator = self.__numerator * frac2.__denominator
        denominator = self.__denominator * frac2.__numerator
        new = Fraction(numerator, denominator)
        return new

    def add(self, frac2):
        """Add the 2 fractions"""
        numerator = self.__numerator * frac2.__denominator + self.__denominator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        new = Fraction(numerator, denominator)
        return new

    def deduct(self,frac2):
        """Find the difference between the two fractions"""
        numerator = self.__numerator * frac2.__denominator-frac2.__numerator * self.__denominator
        denominator = self.__denominator * frac2.__denominator
        new = Fraction(numerator, denominator)
        return new

    def __lt__(self, other):
        """If something is less than or equal to other, return true"""
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __gt__(self, other):
        """If something is less than other, return true"""
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def multiply_fractions(dict):
    """Multiply the fractions entered by user, dict is the dictionary containing fractions"""
    frac1 = input("1st operand: ")
    if frac1 not in dict:
        print(f"Name {frac1} was not found")
        return
    frac2 = input("2nd operand: ")
    if frac2 not in dict:
        print(f"Name {frac2} was not found")
        return

    frac1_number = dict[frac1]
    frac2_number = dict[frac2]

    result = frac1_number.multiply(frac2_number)
    print(f"{dict[frac1]} * {dict[frac2]} = {result}")
    print(f"simplified {result.simplify()}")

def read_file(file_name,dict):
    """Read the file and add the fractions and their name to the list"""
    try:
        data_file=open(file_name, mode = "r")

        for line in data_file:
            line = line.split("=")
            frac_number = line[1].strip().split("/")
            try:
                object = Fraction(int(frac_number[0]),int(frac_number[1]))
                dict[line[0]] = object
            except IndexError:
                print("Error: the file cannot be read.")
                return

    except IOError:
        print("Error: the file cannot be read.")
        return


def main():
    dict = {}
    while True:
        option = input("> ")
        if option == "add":
            frac_number = input("Enter a fraction in the form integer/integer: ")
            frac_name = input("Enter a name: ")
            frac_number = frac_number.split("/")
            frac_object = Fraction(int(frac_number[0]),int(frac_number[1]))
            dict[frac_name] = frac_object
        elif option == "print":
            name = input("Enter a name: ")
            if name in dict:
                print(f"{name} = {dict[name]}")
            else:
                print(f"Name {name} was not found")
        elif option == "list":
            for name in sorted(dict):
                print(f"{name} = {dict[name]}")
        elif option == "*":
            multiply_fractions(dict)
        elif option == "file":
            file_name = input("Enter the name of the file: ")
            read_file(file_name, dict)
        elif option == "quit":
            print("Bye bye!")
            return
        else:
            print("Unknown command!")


if __name__ == '__main__':
    main()