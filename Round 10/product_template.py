"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.

    def __init__(self, name, price,sale=0 ):
        self._name = name
        self._price = price
        self._sale = sale

    def printout(self):
        print(self._name)
        print(f"  price: {self._price:.2f}")
        print(f"  sale%: {self._sale:.2f}")

    def get_price(self):
        return self._price * (1-self._sale/100)

    def set_sale_percentage(self,value):
        self._sale = value


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
