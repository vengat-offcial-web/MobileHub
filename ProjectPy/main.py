from shop import Shop
from utils import title, line, pause

shop = Shop()
while True:
    title()
    print("1. View Mobiles")
    print("2. Add Mobile")
    print("3. Search Mobile")
    print("4. Sell Mobile")
    print("5. Update Stock")
    print("6. Delete Mobile")
    print("7. Sales Report")
    print("8. Exit")
    line()

    try:
        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            shop.view_mobile()
        elif choice == 2:
            shop.add_mobile()
        elif choice == 3:
            shop.search_mobile()
        elif choice == 4:
            shop.sell_mobile()
        elif choice == 5:
            shop.update_stock()
        elif choice == 6:
            shop.delete_mobile()
        elif choice == 7:
            shop.sales.view_report()
        elif choice == 8:
            print("\nThank You For Visiting PVM Mobiles...")
            break
        else:
            print("\nInvalid Choice.")
    except ValueError:
        print("\nPlease Enter Numbers Only.")
    pause()