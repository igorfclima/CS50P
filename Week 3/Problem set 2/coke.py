coins = [5,10,25]
amount = 50
change = 0

while amount != 0:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in coins:
        amount -= insert_coin
        change += insert_coin
    if amount < 0:
        print(f"Change Owed: {change-50}")
        break
    print(f"Amount Due: {amount}")
