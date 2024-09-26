 """
COMP.CS.100
huyen.pham@tuni.fi
"""
def factorial(n):
    """Calcuate the factor for a certain number"""
    for i in range(1,n):
        n = n*i
    return n

def hcf(x,y):
    """find the hcf to cal final result """
    while (y):
        x, y = y, x % y
    return x


def probability(total,drawn):
    """Calcualte the probability of winning"""
    numerator = factorial(total)
    denominator = factorial(total-drawn) * factorial(drawn)

    result = hcf(numerator,denominator)

    return numerator/result, denominator/result


def main():
    total = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))
    (a,b)= probability(total,drawn)
    if total < 0 or drawn < 0:
        print("The number of balls must be a positive number.")
    elif drawn > total:
        print("At most the total number of balls can be drawn.")
    else:
        print(f"The probability of guessing all {drawn} balls correctly is {b:.0f}/{a:.0f}")

if __name__ == '__main__':
    main()