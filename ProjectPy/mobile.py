class Mobile:

    def __init__(self, id, brand, model, ram, storage, price, stock):
        self.id = id
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def sell_mobile(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        return False
    def __str__(self):
         return (
            f"\n{'=' * 35}\n"
            f"Mobile ID : {self.id}\n"
            f"Brand     : {self.brand}\n"
            f"Model     : {self.model}\n"
            f"RAM       : {self.ram}\n"
            f"Storage   : {self.storage}\n"
            f"Price     : ₹{self.price}\n"
            f"Stock     : {self.stock}\n"
            f"{'=' * 35}"
        )