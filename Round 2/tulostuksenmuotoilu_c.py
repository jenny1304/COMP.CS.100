"""
COMP.CS.100
Creator: Huyen Pham
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            # print(i*j, " ", end="")
            print(f"{i*j:4}",end="",sep="")
        print()

if __name__ == "__main__":
    main()
