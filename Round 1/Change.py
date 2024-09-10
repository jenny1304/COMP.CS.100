def main():

    priceString = input("Purchase price: ")
    paidString= input("Paid amount of money: ")

    price = int(priceString)
    paid = int(paidString)

    change = paid - price

    ten = change//10
    five = change % 10 // 5
    two = change % 5 // 2
    sum=0

    if paid>price:
        print("Offer change:")
        if change >=10:
            print(ten,"ten-euro notes")
            sum += ten * 10
        if (change%10) >= 5:
            print(five,"five-euro notes")
            sum += five * 5
        if (change%5) >= 2:
            print(two,"two-euro coins")
            sum += two * 2
        if change - sum > 0:
            print(change - sum,"one-euro coins")
    elif  paid==price or paid<price:
        print("No change")

if __name__ == '__main__':
    main()