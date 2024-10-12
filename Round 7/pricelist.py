"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: Huyen Pham
Email: huyen.pham@tuni.fi
Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.1,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    while True:
        search = input("Enter product name: ")
        find = search.strip()

        if find == "":
            print("Bye!")
            break
        else:
            if find in PRICES:
                print(f"The price of {find} is {PRICES[find]:.2f} e")
            else:
                print(f"Error: {find} is unknown.")

if __name__ == "__main__":
    main()
