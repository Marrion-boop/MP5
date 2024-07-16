import test_user_info
import os
import buying_auction
import selling_auction

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
            Logged_in = False
            print("[1] Login")
            print("[2] Sign-up")
            SubMenuChoice = int(input("Choice: "))

            if SubMenuChoice == 1:
               dummy_name = input("Enter Username: ")
               dummy_passinput = input("Enter Password: ")

               for line in open("buyer_db.txt", "r").readlines():
                    print(line)
                    signin_check = line.split()
                    
                    if dummy_name == signin_check[1] and dummy_passinput == signin_check[2]:
                        os.system('cls')
                        print("Login Successful")
                        Logged_in = True
                    else:
                        os.system('cls')
                        print("Login Failed")
                        Logged_in = False
                    

        
            elif SubMenuChoice == 2:
                #WALA PA MEMBER ID ITERATION
                dummy_email = input("Enter your E-mail: ")
                dummy_name = input("Enter your desired username: ")
                dummy_pass = input("Enter your password: ")
                dummy_address = input("Enter your address: ")
                dummy_phonenum = input("Enter your phone number: ")
                dummy_ship = input("Enter your shipping address: ")
                object = test_user_info.Buyer(dummy_email, dummy_name, dummy_pass, dummy_address,dummy_phonenum, dummy_ship)
                object.putintofile()
                
         
            else:
                print("Input a Valid Number!")
            if Logged_in:
                buyer_menu_object = buying_auction.Menu()
            break

    elif MenuChoice == 2:
        while True:
            Logged_in = False
            print("[1] Login")
            print("[2] Sign-up")
            SubMenuChoice = int(input("Choice: "))

            if SubMenuChoice == 1:
                dummy_name = input("Enter Username: ")
                dummy_pass = input("Enter Password: ")
                #reads the file for username and pass, if it has a match then login sucessful
                for line in open("seller_db.txt", "r").readlines():
                    print(line)
                    signin_check = line.split()
                    
                    if dummy_name == signin_check[1] and dummy_pass == signin_check[2]:
                        os.system('cls')
                        print("Login Successful")
                        Logged_in = True
                    else:
                        os.system('cls')
                        print("Login Failed")
                        Logged_in = False
                    


            elif SubMenuChoice == 2:
                #WALA PA MEMBER ID ITERATION
                dummy_email = input("Enter your E-mail: ")
                dummy_name = input("Enter your desired username: ")
                dummy_pass = input("Enter your password: ")
                dummy_address = input("Enter your address: ")
                dummy_phonenum = input("Enter your phone number: ")
                dummy_bank = input("Enter your bank account number: ")
                dummy_route = input("Enter your bank routing number: ")
                object2 = test_user_info.Seller(dummy_email, dummy_name, dummy_pass, dummy_address,dummy_phonenum, dummy_bank, dummy_route)
                object2.putintofile()
                print("Account Created!")
                input("Press Enter to Continue...")
                os.system('cls')
                break
            else:
                print("Input a Valid Number!")
            if Logged_in:
                seller_menu_object = selling_auction.Menu()
            break

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