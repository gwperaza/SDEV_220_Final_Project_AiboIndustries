'''
Student: Gabriel Peraza
Date: 2/24/2025
File: SDEV 220 - Final Project

Short Desc: This program is designed to allow a potential store manager to view and manage stock and inventory.

Pseudocode:
programActive = 1
Activate empty inventory

While programActive = 1, prompt user to input 'functionChoice'
while functionChoice isn't 1, 2, or 3:
    display error message
    input functionChoice
if functionChoice is 1:
    programActive = 0
    Prompt user for a product name to continue, or '-1' to quit.
    input productName
    while productName != -1:
        input numOfProduct
        input priceForStore
        input priceForCustomer
        calculate totalOrderPrice
        calculate totalPossibleProfits
        inform user that their item has been added
        add all items to 'inventory' to be viewed later
    programActive = 1

elif functionChoice is 2:
    display gathered inventory
    display the total cost of all items for the store and the total profits that would be made through sales.

else:
    programActive = 0
    display thank you message
'''

programActive = 1

class Product:
    def __init__(self, name, stock, storePrice, customerPrice):
        self.name = name
        self.stock = stock
        self.storePrice = storePrice
        self.customerPrice = customerPrice
        self.stockCost = stock * storePrice
        self.stockProfit = stock * customerPrice - self.stockCost

class Inventory():
    def __init__(self):
        self.itemCount = 1
        self.inventory = []
        self.total_cost = 0
        self.total_profit = 0

    def addItem(self, product):
        self.inventory.append(product)
        self.total_cost += product.stockCost
        self.total_profit += product.stockProfit

    def displayInventory(self):
        if not self.inventory:
            print("You have not added anything to the inventory yet.")
        else:
            print("Inventory:\n")
            for product in self.inventory:
                print ("Item #",self.itemCount)
                self.itemCount += 1
                print(f"Name: {product.name}, Stock: {product.stock}, Price of Item for Store: {product.storePrice}, Price of Item for Customer: {product.customerPrice}")
            print("\nTotal Cost: ", self.total_cost, "\nTotal Profits: ", self.total_profit,"\n\n")

storeInventory = Inventory()

while programActive == 1:
    systemChoice = input("Welcome to Aibo Industries!\nWhich system would you like to use?\n1 - Add Products\n2 - View Inventory\n3- Quit Program\nEnter: ")
    while systemChoice not in ["1", "2", "3"]:
        systemChoice = input("Please enter either '1', '2', or '3'.\n1 - Add Products\n2 - View Inventory\n3- Quit Program\nEnter: ")
    if systemChoice == "1":
        productName = str(input("Please enter the product name, or '-1' to quit: "))
        while productName != "-1":
            programActive = 0
            try:
                productStock = int(input("Please enter the amount of this item the store has in inventory: "))
                storePrice = float(input("Please enter the amount this item costs for the store to purchase: "))
                customerPrice = float(input("Please enter how much it costs a customer to buy this product from the store: "))
            except ValueError:
                print("Please enter a valid data type.")
                continue
            fullProduct = Product(productName, productStock, storePrice, customerPrice)
            storeInventory.addItem(fullProduct)
            print("This item has been added to inventory.")
            productName = input("Enter another product name to add a new item, or enter '-1' to quit: ")
        programActive = 1

    elif systemChoice == "2":
        storeInventory.displayInventory()
    else:
        print("This program is finished. Thanks, and good bye!")
        programActive = 0
    
    
    
