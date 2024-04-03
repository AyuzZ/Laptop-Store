from read import *
from write import *
from operations import *

loop = True
while loop:
    # Starting Screen
    print("Welcome to Our Store.")
    print("Please enter one of the following options.")
    print("1. To Sell")
    print("2. To Purchase")
    print("3. Exit")

    # Taking input from the user
    # Doing exception handling
    try:
        options = int(input("Enter one of the above options: "))

        # when customers want to buy
        if options == 1:
            displayStock() #calls the function to show the stock
            sellLaptop() #calls the function to sell laptops
            
        # when the shop is buying
        elif options == 2:
            displayStock()
            loop2 = True
            while loop2:
                print("1. To Re-stock")
                print("2. Buy New Laptops")
                try:
                    buyOption = int(input("Enter one of the above options."))
                    if(buyOption == 1):
                        restock()
                        loop2 = False
                    if(buyOption == 2):
                        buyLaptop()
                        loop2 = False
                    else:
                        print("Please Enter The Numbers 1 or 2")
                except ValueError:
                    print("Please Enter The Numbers 1 or 2")

        # exiting the app    
        elif options == 3:
            print("Have a Great Day Ahead!")
            loop = False

        else:
            print("Please Enter The Numbers From 1 To 3")

    except ValueError:
        print("Please Enter The Numbers From 1 To 3")

