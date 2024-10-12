"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: Huyen Pham
Email: huyen.pham@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    search = input("Enter product name: ")

    search.strip()
    if search == "":
        print("Bye!")
    else:
        if search in PRICES:
            print(f"The price of {search} is {PRICES[search]} e")
        else:
            print(f"Error: {search} is unknown.")


if __name__ == "__main__":
    main()
