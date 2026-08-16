from mobile import Mobile
from data import load_mobiles
from sales import Sales

class Shop:

    def __init__(self):
        self.shop_name = "PVM Mobiles"
        self.mobiles = load_mobiles()
        self.sales = Sales()

    def view_mobile(self):

        if len(self.mobiles) == 0:
            print("\nNo Mobiles Available\n")
            return

        print("\n********** MOBILE LIST **********")

        for mobile in self.mobiles:
            print(mobile)

    def add_mobile(self):

        print("\n========== ADD MOBILE ==========")

        id = int(input("Enter ID : "))
        brand = input("Enter Brand : ")
        model = input("Enter Model : ")
        ram = input("Enter RAM : ")
        storage = input("Enter Storage : ")
        price = int(input("Enter Price : "))
        stock = int(input("Enter Stock : "))

        mobile = Mobile(id, brand, model, ram, storage, price, stock)

        self.mobiles.append(mobile)

        print("\nMobile Added Successfully.")

    def search_mobile(self):

        id = int(input("\nEnter Mobile ID : "))

        for mobile in self.mobiles:

            if mobile.id == id:
                print("\nMobile Found")
                print(mobile)
                return

            print("\nMobile Not Found.")

    def sell_mobile(self):

        id = int(input("\nEnter Mobile ID : "))

        for mobile in self.mobiles:

            if mobile.id == id:

               if mobile.sell_mobile():
                   self.sales.add_sale(mobile)
                   print("Sales :", self.sales.total_sales)
                   print("Revenue :", self.sales.total_revenue)

                   print("\nMobile Sold Successfully.")
               else:
                   print("\nOut of Stock.")
               return
        print("\nMobile Not Found.")

    def update_stock(self):

        id = int(input("\nEnter Mobile ID : "))

        for mobile in self.mobiles:

            if mobile.id == id:

                stock = int(input("Enter New Stock : "))

                mobile.update_stock(stock)

                print("\nStock Updated Successfully.")
                return

        print("\nMobile Not Found.")

    def delete_mobile(self):

        id = int(input("\nEnter Mobile ID : "))

        for mobile in self.mobiles:

            if mobile.id == id:

                self.mobiles.remove(mobile)

                print("\nMobile Deleted Successfully.")
                return

        print("\nMobile Not Found.")