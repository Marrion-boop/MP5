import class_user_info



print("Welcome to the auction house")


while True:
    print("[1] Buy")
    print("[2] Sell")
    print("[3] Auction Winners")
    print("[4] Feedback")
    print("[5] Exit")
    MenuChoice = int(input("Choice: "))

    if MenuChoice == 1:
        while True:
            print("[1] Login")
            print("[2] Sign-up")
            SubMenuChoice = int(input("Choice: "))

            if SubMenuChoice == 1:
                input("Enter Username: ", dummy_name)
                input("Enter Password: ", dummy_pass)
                input("Enter Username: ", dummy_ship)
                #NEED NETO NG FILE HANDLING TO BE COMPLETED
            elif SubMenuChoice == 2:
                dummy_email = input("Enter your E-mail: ")
                dummy_name = input("Enter your desired username: ")
                dummy_pass = input("Enter your password: ")
                dummy_address = input("Enter your address: ")
                dummy_phonenum = input("Enter your phone number: ")
                dummy_ship = input("Enter your shipping address: ")
                object = class_user_info.Buyer(dummy_email, dummy_name, dummy_pass, dummy_address,dummy_phonenum, dummy_ship)
                #WALA PA MEMBER ID ITERATION
            else:
                print("Input a Valid Number!")

    elif MenuChoice == 2:
        while True:
            print("[1] Login")
            print("[2] Sign-up")
            SubMenuChoice = int(input("Choice: "))

            if SubMenuChoice == 1:
                input("Enter Username: ", dummy_name)
                input("Enter Password: ", dummy_pass)
                input("Enter Username: ", dummy_bank)
                input("Enter Password: ", dummy_route)
                #NEED NETO NG FILE HANDLING TO BE COMPLETED
            elif SubMenuChoice == 2:
                dummy_email = input("Enter your E-mail: ")
                dummy_name = input("Enter your desired username: ")
                dummy_pass = input("Enter your password: ")
                dummy_address = input("Enter your address: ")
                dummy_phonenum = input("Enter your phone number: ")
                dummy_bank = input("Enter your bank account number: ")
                dummy_route = input("Enter your bank routing number: ")
                object2 = class_user_info.Seller(dummy_email, dummy_name, dummy_pass, dummy_address,dummy_phonenum, dummy_bank, dummy_route)
                #WALA PA MEMBER ID ITERATION
            else:
                print("Input a Valid Number!")
    elif MenuChoice == 3:
        pass
        #NEED NETO NG FILE HANDLING TO BE COMPLETED
    elif MenuChoice == 4:
        pass
        #NEED NETO NG FILE HANDLING TO BE COMPLETED / SI MAR DITO
    elif MenuChoice == 5:
        break
    else:
        print("Input a Valid Number!")