from itertools import product
from unittest import expectedFailure

print("hello welcome to the accounting system"
      "\n available commands"
      "\n -- balance"
      "\n -- purchase"
      "\n -- sale"
      "\n -- account"
      "\n -- list"
      "\n -- warehouse"
      "\n --review"
      "\n -- end"
      )

balance = 0
warehouse = {}
history = []
product_set = set()

while True:
    command = input("enetr the command ").strip().lower()

    if command == "balance":
        try:
            amount = int(input(" enter amount to add or subtract "))
            balance += amount
            history.append(("balance",amount))
            print(f" balance is updated, new balance = {balance}")
        except ValueError:
            print("invalid amount")

    elif command == "purchase":
        try:
            product = input(" enter product name ").strip()
            price = int(input(" enter the price per unit "))
            quantity = int(input(" enter the quantity purchased "))
            total = price * quantity

            if balance >= total:
                balance -= total
                if product in warehouse:
                    warehouse[product]['quantity'] += quantity
                    warehouse[product]['price'] = price
                else:
                    warehouse[product] = {'price': price,'quantity': quantity}
                history.append(("purchase", product, price,quantity))
                product_set.add(product)
                print(f" purchase successful. new balnce = {balance}")
            else:
                print(" not enough balance ")
        except ValueError:
            print(" invalid input")


    elif command == "sale":
        try:
            product = input("enter the product name ").strip()
            price = int(input("enetr the sale price per unit "))
            quantity = int(input("enter sold quantity "))

            if product in warehouse and warehouse[product]['quantity'] >= quantity:
                total = price * quantity
                balance += total
                warehouse[product]['quantity'] -= quantity
                history.append(("sale", product,price, quantity))
                product_set.add(product)
                print(f" sale successful, new balance is {balance}")
            else:
                print("product not found ")
        except ValueError:
            print(" invalid input ")

    elif command == "account":
        print(f"current balance is {balance}")

    elif command == "list":
        if warehouse:
            print(" warehouse contents ")
            for product in warehouse:
                print(f" {product}: {warehouse[product]['quantity']} units at {warehouse[product]['price']}")
            else:
                print(" warehouse is empty ")

    elif command == "warehouse":
        product = input("enter the product name ").strip()
        if product in warehouse:
            print(f" {product} {warehouse[product]['quantity']} units at {warehouse[product]['price']}")
        else:
            print(" product not found ")

    elif command == "review":
        from_input = input(" from index: ")
        to_ipuut = input(" to index: ")

        try:
            start = int(from_input) if from_input else 0
            end = int(to_ipuut) if to_ipuut else len(history)

            if 0 <= start <= end <= len(history):
                print(f" operations from {start} to {end}: ")
                for i in range (start, end):
                    print(f"{i}: {history[i]}")
                else:
                    print(" invalide index range ")
        except ValueError:
            print(" invalid input, enter numbers only ")

    elif command =="end":
        print(" exiting the program ")
        break

    else:
        print(" unknown command ")