class Manager:
    def __init__(self):
        self.operations = {}

    def assign(self, name, func):
        self.operations[name] = func

    def execute(self, name, *args, **kwargs):
        if name in self.operations:
            return self.operations[name](*args, **kwargs)
        else:
            raise ValueError(f"Task '{name}' not found")



    def sale(self, func):
        def wrapper(*args, **kwargs):
            print(" Processing sale")
            result = func(*args, **kwargs)
            print(" Sale completed")
            return result
        return wrapper

    def purchase(self, func):
        def wrapper(*args, **kwargs):
            print(" Processing purchase")
            result = func(*args, **kwargs)
            print(" Purchase completed")
            return result
        return wrapper

    def balance(self, func):
        def wrapper(*args, **kwargs):
            print(" Checking balance")
            result = func(*args, **kwargs)
            print(" Balance retrieved")
            return result
        return wrapper


if __name__ == "__main__":
    manager = Manager()

    @manager.sale
    def make_sale(amount):
        return f"Sold items worth ${amount}"

    @manager.purchase
    def make_purchase(amount):
        return f"Purchased items worth ${amount}"

    @manager.balance
    def show_balance():
        return "Current balance: $5000"


    manager.assign("sale", make_sale)
    manager.assign("purchase", make_purchase)
    manager.assign("balance", show_balance)
    print(manager.execute("sale", 200))
    print(manager.execute("purchase", 150))
    print(manager.execute("balance"))
