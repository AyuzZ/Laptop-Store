#reading from the file and storing in a dictionary
with open("stock.txt", 'r') as file:
    stock = {}
    laptopIds = 1
    for line in file:
        line = line.replace('\n',"")
        stock.update({laptopIds: line.split(",")})
        laptopIds += 1

boughtLaptop = []
newLaptop = []
companyName = "Komputer Pasal"
companyAddress = "Naya Thimi, Bhaktapur"
companyContact = "9800000000"

# for i in range(1,len(stock)+1):
#     line = ""
#     for each in stock[i]:
#         line = line + each
#     print(str(i) +"." + line)


# print(stock)

# # Extract Laptop Names and Price  and store as key:value pair in dictionary
# laptopPrices = {}
# for i in range(1,len(stock) + 1):
#     laptopPrices[i] = int(stock[i][2][1::])#string slicing to remove the dollar sign
# print(laptopPrices)

# # Extract Laptop Names and available units in stock and store as key:value pair in dictionary
# laptopUnits = {}
# for i in range(1,len(stock) + 1):
#     laptopUnits[i] = int(stock[i][3])
# # print(laptopUnits)

# # Extract Laptop Names and CPU and store as key:value pair in dictionary
# laptopCPUs = {}
# for laptops in stock:
#     laptopCPUs[laptops[0]] = laptops[4]

# # Extract Laptop Names and GPU and store as key:value pair in dictionary
# laptopGPUs = {}
# for laptops in stock:
#     laptopGPUs[laptops[0]] = laptops[5]