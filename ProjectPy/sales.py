class Sales:

    def __init__(self):
        self.total_sales = 0
        self.total_revenue = 0

    def add_sale(self, mobile):

        self.total_sales += 1
        self.total_revenue += mobile.price
    def view_report(self):

        print("\n========== SALES REPORT ==========")
        print(f"Total Mobiles Sold : {self.total_sales}")
        print(f"Total Revenue      : ₹{self.total_revenue}")
        print("*******************************************")