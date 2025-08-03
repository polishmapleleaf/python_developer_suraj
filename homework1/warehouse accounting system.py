import os
import ast

ACCOUNT_FILE = "account_balance.txt"
STOCK_FILE = "warehouse_inventory.txt"
LOG_FILE = "transaction_history.txt"

account_balance = 0.0
warehouse_inventory = {}
transaction_log = []


def load_all_data():
    global account_balance, warehouse_inventory, transaction_log
    try:
        if os.path.exists(ACCOUNT_FILE):
            with open(ACCOUNT_FILE, 'r') as f:
                account_balance = float(f.read())
        if os.path.exists(STOCK_FILE):
            with open(STOCK_FILE, 'r') as f:
                warehouse_inventory = ast.literal_eval(f.read())
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                transaction_log = ast.literal_eval(f.read())
    except Exception as err:
        print(f" Error loading files: {err}")
        print("Initializing system with blank data...")


def save_all_data():
    try:
        with open(ACCOUNT_FILE, 'w') as f:
            f.write(str(account_balance))
        with open(STOCK_FILE, 'w') as f:
            f.write(str(warehouse_inventory))
        with open(LOG_FILE, 'w') as f:
            f.write(str(transaction_log))
    except Exception as err:
        print(f"⚠️ Error saving files: {err}")


def show_main_options():
    print("\n Please select from the available Commands:")
    print("\n credit \n procure \n dispatch \n inventory \n logbook \n exit")


def modify_account():
    global account_balance
    try:
        amount = float(input("Enter amount to credit/debit: "))
        account_balance += amount
        transaction_log.append(f"Account adjusted by {amount}. New balance: {account_balance}")
        print(f" Updated account balance: {account_balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def add_inventory_item():
    global warehouse_inventory, account_balance
    item = input("Item name: ").strip()
    try:
        quantity = int(input("Quantity: "))
        unit_cost = float(input("Cost per item: "))
        total_cost = quantity * unit_cost
        if account_balance >= total_cost:
            warehouse_inventory[item] = warehouse_inventory.get(item, 0) + quantity
            account_balance -= total_cost
            transaction_log.append(f"Acquired {quantity} of {item} at {unit_cost} each. Balance now: {account_balance}")
            print(f" Added to warehouse. {item}: {warehouse_inventory[item]}")
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Invalid quantity or price.")


def remove_inventory_item():
    global warehouse_inventory, account_balance
    item = input("Item name to sell: ").strip()
    if item in warehouse_inventory:
        try:
            quantity = int(input("Quantity: "))
            unit_price = float(input("Selling price per item: "))
            if warehouse_inventory[item] >= quantity:
                warehouse_inventory[item] -= quantity
                account_balance += quantity * unit_price
                transaction_log.append(f"Sold {quantity} of {item} at {unit_price} each. New balance: {account_balance}")
                print(f" Sale processed. Remaining {item}: {warehouse_inventory[item]}")
            else:
                print("Not enough stock.")
        except ValueError:
            print("Invalid input.")
    else:
        print("Item not in inventory.")


def view_inventory():
    print("\n Current Inventory:")
    for item, qty in warehouse_inventory.items():
        print(f"- {item}: {qty}")

def view_logbook():
    print("\n Transaction History:")
    for entry in transaction_log:
        print(f"- {entry}")



def run_company_dashboard():
    load_all_data()
    print(" Welcome to the Company Operations Dashboard")
    while True:
        show_main_options()
        command = input("Select command: ").strip().lower()
        if command == 'credit':
            modify_account()
        elif command == 'procure':
            add_inventory_item()
        elif command == 'dispatch':
            remove_inventory_item()
        elif command == 'inventory':
            view_inventory()
        elif command == 'logbook':
            view_logbook()
        elif command == 'exit':
            save_all_data()
            print("All data saved. Thanks for using this dashboard.")
            break
        else:
            print("Unknown command.")

run_company_dashboard()