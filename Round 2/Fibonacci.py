"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    count = int(input("How many Fibonacci numbers do you want? "))

    num0 = 0
    num1 = 1

    for i in range(1,count + 1):
        print(f"{i}. {num1}")
        num2 = num0+num1
        num0 = num1
        num1 = num2

if __name__ == "__main__":
    main()
