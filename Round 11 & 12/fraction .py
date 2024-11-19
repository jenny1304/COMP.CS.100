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
def main():
    list = []
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    while True:
        fraction = input("")
        if fraction == "":
            break
        else:
            fraction = fraction.split("/")
            list.append(Fraction(int(fraction[0]),int(fraction[1])))


    print("The given fractions in their simplified form:")
    for frac in list:
        print(f"{frac} = {frac.simplify()}")


if __name__ == '__main__':
    main()


