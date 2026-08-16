import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
def line():
    print("-" * 50)
def title():
    clear()
    line()
    print("PVM MOBILE SHOP")
    line()
def pause():
    input("\nPress Enter to Continue...")