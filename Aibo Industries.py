'''
Student: Gabriel Peraza
Date: 3/8/2025
File: Aibo Industries

Short Desc: This program is designed to allow a potential store manager to view and manage stock, inventory, and transactions.

Class diagrams:

---------------------
    class Product

    Attributes:
    - name: str
    - stock: int
    - storePrice: float
    - customerPrice: float

    Operations:
    + __init__()
---------------------
         ^
         |
    (Aggregation)
         |
---------------------
    class Inventory

    Attributes:
    - inventory {}
    - product: str
    - inventoryDisplay: str
    - addCost: float
    - total_cost: float
    - potential_profit: float
    - addProfits: float
    - itemCount: int

    Operations:
    + __init__()
    + addItem()
    + displayInventory()
---------------------
         ^
         :
    (Dependency)
         :
---------------------
    class Transaction

    Attributes:
    + money: float
    - item: str
    - amount: int

    Operations:
    + __init__()
    - make_transaction()
    + getmoney()
---------------------

Documentation of Testing:
    This program has been thoroughly tested with countless input types and values. It is to my best knowledge
    that this program is completely impossible to crash.

    Sample input (Add Items):
        
        1.
        Product Name: !!!
        Number to order: 3
        Costs the store: 5
        Costs the customer: 9
        
        Output: *Special characters detected in product name



        2.
        Product Name: Apple
        Number to order: -5
        Costs the store: 2
        Costs the customer: 8
        
        Output: *Invalid values detected in one or more fields



        3.
        Product Name: Television
        Number to order: 20
        Costs the store: 200 (20 televisions cost more than the starting money amount of 500)
        Costs the customer: 350
        
        Output: *Invalid values detected in one or more fields

        

        4.
        Product Name: Toy
        Number to order: 7
        Costs the store: 4
        Costs the customer:
        
        Output: *Please ensure all fields are filled correctly before submission


        
        5.
        Product Name: Tools
        Number to order: 15
        Costs the store: 8
        Costs the customer: 12
        
        Output: Item added successfully

    Sample input (Make Transaction):
        
        1.
        Product Name: !!!
        Amount Ordered: 5
        
        Output: *Special characters detected in product name


        
        2.
        Product Name: ItemNotAdded
        Amount Ordered: 3
        
        Output: *Product not found




        3.
        Product Name: Tools
        Amount Ordered: 20 (More than in stock)
        
        Output: *Valid stock values are any integer from 1 to 15

        

        4.
        Product Name: Tools
        Amount Ordered: abcd
        
        Output: *Valid stock values are any integer from 1 to 15

        
    
        5.
        Product Name: Tools
        Amount Ordered: 4
        
        Output: *Qty 4 of product Tools purchased

'''

# Imports valuable tools that grant us access to GUI development
import tkinter as tk

# Allows us to set up a product's attributes including it's name, number in inventory, cost for the company,
# and how much it costs a customer to buy the item.
class Product:
    def __init__(self, name, stock, storePrice, customerPrice):
        self.name = name
        self.stock = stock
        self.storePrice = storePrice
        self.customerPrice = customerPrice

        # These last two calcuate how much it costs the store to order the amount in inventory, and how much
        # money is made off of each purchase.
        self.stockCost = stock * storePrice
        self.stockProfit = stock * customerPrice - self.stockCost

# Allows us to set up and store created products into an inventory system.
class Inventory:

    # Prepares the storage unit for our items
    def __init__(self):
        self.inventory = {}

    # Adds the provided item into our prepared inventory
    def addItem(self, product):
        self.inventory[product.name] = product

    # Creates and displays the inventory whenever the given button is pressed
    def displayInventory(self):

        # Initial setup of the display variable that sends a message to the user
        inventoryDisplay = ""

        # If nothing is in the inventory when the user clicks the button, the display makes them aware of that
        if not self.inventory:
            inventoryDisplay = "You have not added anything to the inventory yet."
        
        # Otherwise, a series of calculations occur.
        else:

            # First, variables to calculate the total costs for the stores entire inventory are initiated
            self.addCost = 0
            self.total_cost = 0
            self.potential_profit = 0

            # For every product found in the inventory, the cost of all of its stock is added
            # to the proper variable and then stored for later
            for product in self.inventory.values():
                self.addCost += product.stockCost
                self.total_cost = self.addCost
            
            # The same process then occurs for the profits, in other words the money made minus expenses
            # for each product
            self.addProfits = 0
            for product in self.inventory.values():
                self.addProfits += product.stockProfit
                self.potential_profit = self.addProfits
            
            # Now it is time to display our entire inventory and the calculations we made to the user
            # The inventory is shown with all items numbered in the order they were added, with calculations
            # shown at the very bottom

            # A variable is initiated to number the items, starting at 1
            self.itemCount = 1

            # For every product stored, the calculated item number is shown and increased
            for product in self.inventory.values():
                inventoryDisplay += f"\n\n\nItem #{self.itemCount}\n"
                self.itemCount += 1

                # Now all of the gathered data is displayed under it
                inventoryDisplay+= f"\nName: {product.name} \nStock: {product.stock} \nPrice of Item for Store: ${product.storePrice:.2f} \nPrice of Item for Customer: ${product.customerPrice:.2f}"
            inventoryDisplay+= f"\n\n\nTotal Cost: ${self.total_cost:.2f}\nPotential Profits: ${self.potential_profit:.2f}"
        
        # This initiates the GUI text that actually makes our communication variable visible to the user
        inventory.config(state="normal")
        inventory.delete(1.0, tk.END)
        inventory.insert(tk.END, inventoryDisplay)
        inventory.config(state="disabled")

# Stores our money, and allows us to add to it when customers buy items
class Transaction:

    # Our store starts with $500 to buy stock with
    money = 500

    # Accepts values for the item and number of the item being bought, then starts the calculation
    # for the money made from the purchase
    def __init__(self, item, amount):
        self.item = item
        self.amount = int(amount)
        self.make_transaction()
    
    # Subtracts from stock when purchases are made, recalculates the stock cost and profits, then grants the
    # money from the purchase
    def make_transaction(self):
        boughtproduct = storeInventory.inventory[self.item]
        boughtproduct.stock -= self.amount
        boughtproduct.stockCost = boughtproduct.stock * boughtproduct.storePrice
        boughtproduct.stockProfit = (boughtproduct.stock * boughtproduct.customerPrice) - boughtproduct.stockCost
        Transaction.money += boughtproduct.customerPrice*self.amount

    # Allows other functions in the program to access the money variable
    @staticmethod
    def get_money(cls):
        return cls.money

# Creates an instance of the Inventory class to be accessed by future functions
storeInventory = Inventory()

# Whevener a button is clicked, clears the main page from all of its data in preparation for new page data
def init_page():
    addButton.place_forget()
    payButton.place_forget()
    viewButton.place_forget()
    budget.place_forget()
    budgetLabel.place_forget()

    # The quit button is reworked to route to the main page instead of exiting the program
    quitButton.config(text="Back", command=initialize_main)

# Sets up the page for item additions whenever that given button is pressed
def add_items():
    init_page()
    header.config(text="Add Items:")
    # An entry field and a descriptory label is placed on the screen for every necessary entry field for adding items
    # The values of the entry fields are also erased in case the user typed something earlier and then backed out
    nameLabel.place(relx=0.55, rely=0.25, anchor="e")
    nameEntry.place(relx=0.65, rely=0.25, anchor="center")
    nameEntry.delete(0, tk.END)

    stockLabel.place(relx=0.55, rely=0.4, anchor="e")
    stockEntry.place(relx=0.65, rely=0.4, anchor="center")
    stockEntry.delete(0, tk.END)

    costLabel.place(relx=0.55, rely=0.55, anchor="e")
    costEntry.place(relx=0.65, rely=0.55, anchor="center")
    costEntry.delete(0, tk.END)

    saleLabel.place(relx=0.55, rely=0.7, anchor="e")
    priceEntry.place(relx=0.65, rely=0.7, anchor="center")
    priceEntry.delete(0, tk.END)

    # The submit button is also placed onto the screen in this step
    submitButton.place(relx=0.5, rely=0.9, anchor="center")
    submitButton.config(command=check_inputs)

# Whenever the submit button is pressed, the program ensures that all given values are valid.
# If so, the provided inputs are submitted into the inventory
def check_inputs():
    productName = nameEntry.get()
    productStock = stockEntry.get()
    storeCost = costEntry.get()
    customerPrice = priceEntry.get()
    try:
        # First, the types of the data are tested
        productStock = int(productStock)
        storeCost = float(storeCost)
        customerPrice = float(customerPrice)

        # If the data types are all valid, then the values of the data are tested
        if productName.isalnum() == False:
            raise ValueError
        if productName in storeInventory.inventory and storeInventory.inventory[productName].stock != 0:
            raise ValueError
        if productStock < 0 or storeCost < 0 or customerPrice < 0:
            raise ValueError
        if  productStock * storeCost > Transaction.money:
            raise ValueError

        # If all is well, money is subtracted from the store to pay for the items, the item is added to inventory,
        # and the entry fields are all cleared for resubmission if desired
        Transaction.money -= productStock * storeCost
        popupNotice.config(text="Item added successfully", fg="#FAF9F6")
        popupNotice.place(relx=0.5, rely=0.78, anchor="center")
        nameEntry.delete(0, tk.END)
        stockEntry.delete(0, tk.END)
        costEntry.delete(0, tk.END)
        priceEntry.delete(0, tk.END)
        fullProduct = Product(productName, productStock, storeCost, customerPrice)
        storeInventory.addItem(fullProduct)

    # If an error is detected, the user is informed of what went wrong
    except ValueError:
        if productName.isalnum() == False and productName != "":
            popupNotice.config(text="*Special characters detected in product name", fg="red")
        elif not productName or not productStock or not storeCost or not customerPrice:
            popupNotice.config(text="*Please ensure all fields are filled correctly before submission", fg="red")
        elif productName in storeInventory.inventory:
            popupNotice.config(text="*Product already in inventory", fg="red")
        else: 
            popupNotice.config(text="*Invalid values detected in one or more fields", fg="red")
        popupNotice.place(relx=0.5, rely=0.78, anchor="center")

# Sets up the page for transactions whenever that given button is pressed
def make_transaction():
    header.config(text="Make Transaction:")
    init_page()

    # Like the add item page, entry fields, labels, and the submit button are placed on the screen as needed
    productNameLabel.place(relx=0.55, rely=0.4, anchor="e")
    nameEntry.place(relx=0.65, rely=0.4, anchor="center")
    nameEntry.delete(0, tk.END)

    purchaseAmountLabel.place(relx=0.55, rely=0.55, anchor="e")
    amountEntry.place(relx=0.65, rely=0.55, anchor="center")
    amountEntry.delete(0, tk.END)

    submitButton.place(relx=0.5, rely=0.9, anchor="center")
    submitButton.config(command=check_transaction_inputs)

# Like item entry, transaction submissions must be checked before they are allowed to progress in the program
def check_transaction_inputs():
    
    # Entries are retrieved for testing
    nameBought = nameEntry.get()
    amountBought = amountEntry.get()
    try:
        # Like before, the type of data is validated first, then the values
        amountBought = int(amountBought)
        if nameBought.isalnum() == False:
            raise ValueError
        if not nameBought or not amountBought or storeInventory.inventory.get(nameBought) is None:
            raise ValueError
        if amountBought <= 0 or amountBought > storeInventory.inventory[nameBought].stock:
            raise ValueError
        
        # If data is deemed valid, the transaction goes through and the data is sent to the Transaction class
        Transaction(nameEntry.get(), amountEntry.get())
        nameEntry.delete(0, tk.END)
        amountEntry.delete(0, tk.END)
        transactionSubmitPop.config(text=f"Qty {amountBought} of product {nameBought} purchased", fg="#FAF9F6")
    except ValueError:
        if nameBought.isalnum() == False and nameBought != "":
            transactionSubmitPop.config(text="*Special characters detected in product name", fg="red")
        elif not nameBought or not amountBought:
            transactionSubmitPop.config(text="*Please ensure both fields are filled correctly before submission", fg="red")
        elif storeInventory.inventory.get(nameBought) is None:
            transactionSubmitPop.config(text="*Product not found", fg="red")
        elif storeInventory.inventory[nameBought].stock == 0:
            transactionSubmitPop.config(text=f"*Product {nameBought} is out of stock", fg="red")
        else:
            transactionSubmitPop.config(text=f"*Valid stock values are any integer from 1 to {storeInventory.inventory[nameBought].stock}", fg="red")
    transactionSubmitPop.place(relx=0.5, rely=0.7, anchor="center")
    

# If the inventory button is pressed, the page is cleared and a text box appears to store inventory data in
def view_inventory():
    init_page()
    header.config(text="Inventory:")
    inventory.place(relx=0.5, rely=0.5, anchor="center")
    storeInventory.displayInventory()

# Clears the page of data in order to set up the main page
def initialize_main():
    header.config(text="Welcome to Aibo Industries!")
    addButton.place(relx=0.5, rely=0.4, anchor="center")
    payButton.place(relx=0.5, rely=0.6, anchor="center")
    viewButton.place(relx=0.5, rely=0.8, anchor="center")

    # On the main page, the Quit button is reset back to its quit function instead of the back function
    # that is present elsewhere
    quitButton.config(text="Quit", command=main.quit)

    # Money is tracked every time the user returns to the main page, ensuring that it always displays correctly
    budget.config(text = f"${Transaction.money:.2f}")

    budget.place(relx=0.98, rely=0.02, anchor="ne")
    budgetLabel.place(relx=0.985, rely=0.08, anchor="ne")

    # Every single piece of GUI that might have been added for another page has to be cleared for the main page
    nameLabel.place_forget()
    nameEntry.place_forget()
    stockEntry.place_forget()
    costEntry.place_forget()
    priceEntry.place_forget()
    stockLabel.place_forget()
    costLabel.place_forget()
    saleLabel.place_forget()
    submitButton.place_forget()
    popupNotice.place_forget()
    inventory.place_forget()
    productNameLabel.place_forget()
    nameEntry.place_forget()
    purchaseAmountLabel.place_forget()
    amountEntry.place_forget()
    transactionSubmitPop.place_forget()

# Sets up the window size, title, and background color of the application
main = tk.Tk()
main.title("Aibo Industries")
main.geometry("700x400")
main.configure(bg="#1F3B4D")
main.resizable(0, 0)

# All GUI elements are specially configured to the program's needs
# Elements necessary for the main page are also placed in their appropriate spots for startup
header = tk.Label(main, text="Welcome to Aibo Industries!", font=("Courier", 20), bg="#1F3B4D", fg="#FAF9F6")
header.place(relx=0.5, rely=0.1, anchor="center")

addButton = tk.Button(main, height=2, width=15, text="Order Items", font=("Courier", 12), bg="#4492BD", fg="#FAF9F6", activebackground="#2E7297", command=add_items)
addButton.place(relx=0.5, rely=0.4, anchor="center")

payButton = tk.Button(main, height=2, width=15, text="Transaction", font=("Courier", 12), bg="#4492BD", fg="#FAF9F6", activebackground="#2E7297", command=make_transaction)
payButton.place(relx=0.5, rely=0.6, anchor="center")

viewButton = tk.Button(main, height=2, width=15, text="View Inventory", font=("Courier", 12), bg="#4492BD", fg="#FAF9F6", activebackground="#2E7297", command=view_inventory)
viewButton.place(relx=0.5, rely=0.8, anchor="center")

quitButton = tk.Button(main, height=2, width=8, text="Quit", font=("Courier", 10), bg="#4492BD", fg="#FAF9F6", activebackground="#2E7297", command=main.quit)
quitButton.place(relx=0.98, rely=0.98, anchor="se")

nameLabel = tk.Label(main, text="Product name: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
nameEntry = tk.Entry(main)

stockLabel = tk.Label(main, text="Number to order: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
stockEntry = tk.Entry(main)

costLabel = tk.Label(main, text="Costs the store: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
costEntry = tk.Entry(main)

saleLabel = tk.Label(main, text="Costs the customers: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
priceEntry = tk.Entry(main)

submitButton = tk.Button(main, height=2, width=15, text="Submit", font=("Courier", 12), bg="#4492BD", fg="#FAF9F6", activebackground="#2E7297", command=check_inputs)

popupNotice = tk.Label(main, text="", font=("Courier", 12), bg="#1F3B4D", fg="red")

transactionSubmitPop = tk.Label(main, font=("Courier", 12), bg="#1F3B4D", fg="red", text="")

productNameLabel = tk.Label(main, text="Product Name: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
nameEntry = tk.Entry(main)

purchaseAmountLabel = tk.Label(main, text="Amount Ordered: ", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6", justify="left")
amountEntry = tk.Entry(main)

inventory = tk.Text(main, width=85, height=17, state="disabled")

budget = tk.Label(main, text = f"${Transaction.money:.2f}", width=8, height=1)
budget.config(state="disabled")
budget.place(relx=0.98, rely=0.02, anchor="ne")

budgetLabel = tk.Label(main, text="Budget", font=("Courier", 15), bg="#1F3B4D", fg="#FAF9F6")
budgetLabel.place(relx=0.985, rely=0.08, anchor="ne")

# Finally, the main page is initiated, launching the GUI program
main.mainloop()