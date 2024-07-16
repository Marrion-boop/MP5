#PAGKALOGIN DITO MAPUPUNTA, NEED NG FILE HANDLING NETO TO BE COMPLETED, PAG MERON NA FILE HANDLING NG SELLER ITEMS AKO NA MAGLALAGY NG MENU
def Buy():
    buy=input("What is The item that you want to buy?")
    f = open("itemlist.txt", "r")

    lines = f.readline()
    while True:
            line = f.readline()
            
            if not line:
                break
            else:
             print("You Were HEAR")
             goodboy=(eval(lines))
             if goodboy[0].upper()==buy.upper():
                print(goodboy[0])
                break
             else:
                 continue
    f.close()

def Menu():
    while True:
        print("Hello Buyer! What would you like to do?")
        print("[1] Buy items in auction")
        print("[2] Exit")
        Buyer_Choice = int(input("Choice: "))
        if Buyer_Choice == 1:
            Buy()
        elif Buyer_Choice == 2:
             break
        else:
            print("Input a Valid Number!")