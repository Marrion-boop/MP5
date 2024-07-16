#PAGKALOGIN DITO MAPUPUNTA, NEED NG FILE HANDLING NETO TO BE COMPLETED, PAG MERON NA FILE HANDLING NG SELLER ITEMS AKO NA MAGLALAGY NG MENU
import os

def Sell():
    f = open("itemlist.txt", "a")
    name = input("Enter your item name: ")
    price = input("Enter your item price: ")
    rank = input("Enter your item rank: ")
    lines = (name +'\n'+ price +'\n'+ rank)
    f.writelines(lines)
    f.close()


def Menu():
    while True:
        print("Hello Seller! What would you like to do?")
        print("[1] Sell items in auction")
        print("[2] Exit")
        Seller_Choice = int(input("Choice: "))

        if Seller_Choice == 1:
            Sell()
        elif Seller_Choice == 2:
            break
        else:
            print("Input a Valid Number!")

    