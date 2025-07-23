def groceries():
    cart = {}

    while True:
            try:
                item = input().upper().strip()

                cart[item] = cart.get(item, 0) + 1
            except EOFError:
                break
    sorted_items = sorted(cart.items())
    for fruits,quant in sorted_items.items():
        print(f"{quant} {fruits} ")
groceries()
