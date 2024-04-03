from read import *
def updateStockFile(stock):
    with open("stock.txt",'w') as file:
        for values in stock.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
            
def sellNote(cName, cNumber, cAddress, boughtLaptop, totalCost, shippingCost, totalAmount, localTime):
    #writing the receipt to a file
    fileName = cName+"_"+localTime+".txt"
    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")
    with open(fileName,'w') as file:
        file.write("\n"+companyName.center(50))
        file.write("\n"+companyAddress.center(50))
        file.write("\n"+companyContact.center(50))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("RECEIPT".center(50))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Laptop".ljust(20) + "Brand".ljust(15) + "Units".ljust(10) + "Unit Price".ljust(10)+"\n")
        for each in boughtLaptop:
            unitPrice = int(each[2].replace("$",""))
            lineTotal = "$"+str(each[3] * unitPrice)
            file.write(each[0].ljust(20) + each[1].ljust(15) + str(each[3]).ljust(10) + each[2].rjust(10)+ lineTotal.rjust(10)+"\n")
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Total Cost".ljust(45)+("$"+str(totalCost)).rjust(10))
        file.write("\nShipping Cost".ljust(45)+("$"+str(shippingCost)).rjust(10))
        file.write("\nTotal Cost including Shipping".ljust(45)+("$"+str(totalAmount)).rjust(10))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Customer :".ljust(20) + cName)
        file.write("\nContact :".ljust(20) + cNumber)
        file.write("\nAddress :".ljust(20) + cAddress)
        file.write("\n"+localTime.center(50))
        file.write("\n--------------------------------------------------------------------\n")

def buyNote(cName, cAddress, localTime, newLaptop, netAmount, grossAmount):
    fileName = cName+"_"+localTime+".txt"
    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")
    with open(fileName,'w') as file:
        file.write("\n"+cName.center(50))
        file.write("\n"+cAddress.center(50))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("RECEIPT".center(50))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Laptop".ljust(20) + "Brand".ljust(15) + "Units".ljust(10) + "Unit Price".ljust(10)+ "Total".ljust(10) +"\n")
        for each in newLaptop:
            unitPrice = int(each[2].replace("$",""))
            lineTotal = "$"+str(each[3] * unitPrice)
            file.write(each[0].ljust(20) + each[1].ljust(15) + str(each[3]).ljust(10) + each[2].rjust(10) + lineTotal.rjust(10)+"\n")
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Net Amount(Excludes VAT)".ljust(45)+("$"+str(netAmount)).rjust(10))
        file.write("\nVAT applicable".ljust(45)+("13%".rjust(10)))
        file.write("\nGross Amount(Includes VAT)".ljust(45)+("$"+str(grossAmount)).rjust(10))
        file.write("\n--------------------------------------------------------------------\n")
        file.write("Customer :".ljust(20) + companyName+"\n")
        file.write("Contact :".ljust(20) + companyContact+"\n")
        file.write("Address :".ljust(20) + companyAddress+"\n")
        file.write(localTime.center(50))
        file.write("\n--------------------------------------------------------------------\n")

        