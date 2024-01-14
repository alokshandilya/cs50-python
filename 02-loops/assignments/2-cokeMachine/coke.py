def main():
    amount_due = 50
    print("Amount Due:", amount_due)

    while amount_due > 0:
        inserted_coin = int(input("Insert Coin: "))
        if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5:
            amount_due -= inserted_coin
        if amount_due > 0:
            print("Amount Due:", amount_due)
    print("Change Owed:", -amount_due)


main()
