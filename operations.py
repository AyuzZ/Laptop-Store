from read import *
from write import *
import datetime

# opening stock.txt on read mode
def displayStock():
    print("\nWe have the following laptops available in our stock.")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("S.N".ljust(8)+"Laptop".ljust(20)+"Brand".ljust(20)+"Price".ljust(20)+"Units".ljust(20)+"CPU".ljust(20)+"GPU".ljust(20))
    print("---------------------------------------------------------------------------------------------------------------------------")
    for i in range(1,len(stock)+1):
        line = ""  
        for j in range(len(stock[i])):
            name = stock[i][j].ljust(20)
            line = line + name
        lid = str(i).ljust(8)
        print(lid + line)
        print("---------------------------------------------------------------------------------------------------------------------------")

# function to chose the laptop name
def sellLaptop():
    try:
        laptopId = int(input("Enter the id of the laptop you are selling: "))
        
        if laptopId > 0 and laptopId <= len(stock):
            if int(stock[laptopId][3]) == 0:
                print("Given Laptop Is Out Of Stock. Please Enter Another Id")
                sellLaptop()
            else:
                laptopUnit(laptopId)        
        else:
            print("Given Id doesn't with our stock.\nRe-check the Id of the laptop")
            sellLaptop()
    except ValueError:
        print("Please Enter Correct Id.")
        sellLaptop()

# function to chose the numbers of laptops you want to sell                       
def laptopUnit(laptopId):
    try:
        laptopCount = int(input("Enter the unit of laptops you are selling: "))
        if laptopCount <= 0 :
            print("Please enter value greater than 0.")
            laptopUnit(laptopId)
        elif laptopCount <= int(stock[laptopId][3]): #need to check if the amount is available in the stock or not
            #update the list of laptops getting sold(bought by customer)
            if len(boughtLaptop) == 0:
                boughtLaptop.append([stock[laptopId][0], stock[laptopId][1], stock[laptopId][2], laptopCount, stock[laptopId][4], stock[laptopId][5]])
            else:
                lapName = []
                for each in boughtLaptop:
                    lapName.append(each[0])
                if stock[laptopId][0] in lapName:
                    for each in boughtLaptop: #looping to find the laptop to add the quantity in
                        if stock[laptopId][0] == each[0]: #matching the name
                            each[3] = each[3] + laptopCount    
                else:
                    boughtLaptop.append([stock[laptopId][0], stock[laptopId][1], stock[laptopId][2], laptopCount, stock[laptopId][4], stock[laptopId][5]])
            # print("you are currently buying this.",boughtLaptop) 

            # subtracting the bought units from the stock - updating the stock list
            stock[laptopId][3] = str(int(stock[laptopId][3]) - laptopCount)
            updateStockFile(stock)
            loop = True
            while True:
                continueBuying = input("Press Y to continue shopping.\nPress N to create bill.")
                if continueBuying.lower() == "y":
                    loop = False
                    displayStock();
                    sellLaptop();
                elif continueBuying.lower() == "n":
                    loop = False
                    sellTransaction(boughtLaptop)
                else:
                    print("Enter Only Y or N")
        else:
            print("Please enter the amount availabe with us.")
            laptopUnit(laptopId)
    except ValueError:
        print("Please Enter Numbers Only.")
        laptopUnit(laptopId)

def sellTransaction(boughtLaptop):
    cName = input("Enter Customer's Full Name: ")
    cNumber = input("Enter Customer's Phone number: ")
    cAddress = input("Enter Customer's Address: ")
    print("\n"+companyName.center(50))
    print(companyAddress.center(50))
    print(companyContact.center(50))
    print("\n--------------------------------------------------------------------\n")
    print("RECEIPT".center(50))
    print("\n--------------------------------------------------------------------\n")
    print("Laptop".ljust(20) + "Brand".ljust(15) + "Units".ljust(10) + "Unit Price".ljust(10) + "Total".ljust(10))
    totalCost = 0
    shippingCost = 100
    for each in boughtLaptop: 
        unitPrice = int(each[2].replace("$",""))
        lineTotal = "$"+str(each[3] * unitPrice)
        print(each[0].ljust(20) + each[1].ljust(15) + str(each[3]).ljust(10) + each[2].rjust(10) +lineTotal.rjust(10))
        totalCost += (each[3] * unitPrice)
        # removing $ and converting it to int
    print("\n--------------------------------------------------------------------\n")
    print("Total Cost".ljust(45)+("$"+str(totalCost)).rjust(10))
    print("Shipping Cost".ljust(45)+("$"+str(shippingCost)).rjust(10))
    totalAmount = totalCost + shippingCost
    print("Total Cost including Shipping".ljust(45)+("$"+str(totalAmount)).rjust(10))
    print("\n--------------------------------------------------------------------\n")
    print("Customer :".ljust(20) + cName)
    print("Contact :".ljust(20) + cNumber)
    print("Address :".ljust(20) + cAddress)
    time = datetime.datetime.now()
    localTime = time.strftime("%c") # .strftime("%c") - Local version of date and time
    print(localTime.center(50))
    print("\n--------------------------------------------------------------------\n")
    sellNote(cName, cNumber, cAddress, boughtLaptop, totalCost, shippingCost, totalAmount, localTime)

def restock():
    try:
        laptopId = int(input("Enter the id of the laptop you are re-stocking."))
        if laptopId > 0 and laptopId <= len(stock):
            laptopQuantity = int(input("Enter the quantity you want to buy."))
            newLaptop.append([stock[laptopId][0],stock[laptopId][1],stock[laptopId][2],laptopQuantity,stock[laptopId][4],stock[laptopId][5]])
            stock[laptopId][3] = str(int(stock[laptopId][3]) + laptopQuantity)
            updateStockFile(stock)
            loop = True
            while loop:
                continueBuying = input("Do you want to restock more laptops.\nEnter Y to Continue.\nEnter N to Print Receipt: ")
                if continueBuying.lower() == "y":
                    loop = False
                    restock()
                elif continueBuying.lower() == "n":
                    loop = False
                    buyTransaction(newLaptop)
                else:
                    print("Enter Only Y or N")

        else:
            print("Given Id doesn't with our stock.\nRe-check the Id of the laptop")
            restock()

    except ValueError:
        print("Please Enter Numbers Only")
        restock()


def buyLaptop():
    newLaptopName = input("Enter the Name of the laptop you're looking to buy: ")
    newLaptopBrand = input("Enter the Brand of the laptop: ")
    newLaptopCPU = input("Enter the CPU of the laptop: ")
    newLaptopGPU = input("Enter the GPU of the laptop: ")
    laptopPriceUnits(newLaptopName, newLaptopBrand, newLaptopCPU, newLaptopGPU)

def laptopPriceUnits(newLaptopName, newLaptopBrand, newLaptopCPU, newLaptopGPU):
    try:
        newLaptopPrice = int(input("Enter the Price of the laptop: "))
        newLaptopUnits = int(input("Enter the Quantity of the laptops: "))
        
        #update the list of laptops getting bought by us
        if len(newLaptop) == 0:
            newLaptop.append([newLaptopName, newLaptopBrand, "$"+str(newLaptopPrice), newLaptopUnits, newLaptopCPU, newLaptopGPU])
        else:
            lapName = []
            for each in newLaptop:
                lapName.append(each[0].lower())#getting the names of the laptops that we are buying
            if newLaptopName.lower() in lapName:
                for each in newLaptop: #looping to find the laptop to add the quantity in
                    if newLaptopName == each[0]: #matching the name
                        each[3] = each[3] + newLaptopUnits    
            else:
                newLaptop.append([newLaptopName, newLaptopBrand, "$"+str(newLaptopPrice), newLaptopUnits, newLaptopCPU, newLaptopGPU])
        
        # print("you are currently buying this.",newLaptop)

        #for updating our existing stock dictionary
        lapNames = []
        for i in range(1,len(stock)+1):
            lapNames.append(stock[i][0]) #getting the names of the laptops that we already have in stock
        if newLaptopName in lapNames:
            for i in range(1,len(stock)+1): #looping to look through the dictionary containing our stock to find the matching one and adding the recently bought quantity to the one we had
                if stock[i][0] == newLaptopName:
                    stock[i][3] += newLaptopUnits
        else:
            stock[len(stock)+1] = [newLaptopName, newLaptopBrand, "$"+str(newLaptopPrice), newLaptopUnits, newLaptopCPU, newLaptopGPU]
        updateStockFile(stock)
        loop = True
        while loop:
            continueBuying = input("Do you want to buy more laptops.\nEnter Y to Continue.\nEnter N to Print Receipt: ")
            if continueBuying.lower() == "y":
                loop = False
                buyLaptop()
            elif continueBuying.lower() == "n":
                loop = False
                buyTransaction(newLaptop)
            else:
                print("Enter only Y or N.")
    except ValueError:
        print("Please Enter Numerical Value For Price and Units.")
        laptopPriceUnits(newLaptopName, newLaptopBrand, newLaptopCPU, newLaptopGPU)

def buyTransaction(newLaptop):
    cName = input("Enter Company's Name: ")
    cAddress = input("Enter the Company's address: ")
    print("\n"+cName.center(50))
    print(cAddress.center(50))
    print("\n--------------------------------------------------------------------\n")
    print("RECEIPT".center(50))
    print("\n--------------------------------------------------------------------\n")
    print("Laptop".ljust(20) + "Brand".ljust(15) + "Units".ljust(10) + "Unit Price".ljust(10) + "Total".ljust(10))
    netAmount = 0
    for each in newLaptop: 
        unitPrice = int(each[2].replace("$",""))
        lineTotal = "$"+str(each[3] * unitPrice)
        print(each[0].ljust(20) + each[1].ljust(15) + str(each[3]).ljust(10) + each[2].rjust(10) + lineTotal.rjust(10))
        netAmount += (each[3] * unitPrice)
        # removing $ and converting it to int
    print("\n--------------------------------------------------------------------\n")
    print("Net Amount(Excludes VAT)".ljust(45)+("$"+str(netAmount)).rjust(10))
    print("VAT applicable".ljust(45)+("13%".rjust(10)))
    grossAmount = netAmount + (0.13 * netAmount)
    print("Gross Amount(Includes VAT)".ljust(45)+("$"+str(grossAmount)).rjust(10))
    print("\n--------------------------------------------------------------------\n")
    print("Customer :".ljust(20) + companyName)
    print("Contact :".ljust(20) + companyContact)
    print("Address :".ljust(20) + companyAddress)
    time = datetime.datetime.now()
    localTime = time.strftime("%c") # .strftime("%c") - Local version of date and time
    print(localTime.center(50))
    print("\n--------------------------------------------------------------------\n")
    buyNote(cName, cAddress, localTime, newLaptop, netAmount, grossAmount)