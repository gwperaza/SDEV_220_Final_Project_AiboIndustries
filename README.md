Welcome to Aibo Industries!

This is a project designed to simulate stock and inventory management of a store. It can be used to practice business decisions, to train potential managers, or just for fun.

# Installation:
  This project only uses tkinter. Besides the main python file, no additional files or programs need be downloaded in order to use this application.

# How to use:
  This program has four main pages: Main Page, Order Items, Make Transaction, and View Inventory.

  Main page:
  The program will load up to the main page upon execution of the python file.
  Take note of the budget on the upper right hand corner of the screen. This is the amount of money that the store has. You can only spend this amount of money, however you can
  increase your money by making transactions.
  Simply select a button (Order Items, Make Transaction, View Inventory, or Quit) to proceed.

  Order Items:
  Here you can get products ready for purchase. You will be prompted to enter a product name, the number of stock to order, the amount that an indiviual item costs the store
  to purchase, and the amount you will sell it to your customers for. Simply enter an alphanumeric value for the item name, an integer for the stock amount, and floats for
  the cost and sale entries. Ensure that there are no blanks, special characters, or incorrect data types, and also that you have enough money to buy the proposed amount of
  stock. If this is not done, the program will display an error message and you will have to edit your values before submission. Lastly, items must be unique to be added to
  inventory. You will receive an error popup if you try to add an item with the same name as a previous entry to the inventory. The only exception to this is if the product's
  stock has reached zero. In this case, the item's stock and sale values can be re-entered by simply inputting the new values after entering the same product name.

  Transaction:
  This is how your store will gain money. After clicking on the button, the program will prompt you for the item name and the amount that the customer ordered. Items must be
  added to inventory using the 'Order Items' page before they can be used in transactions. Ensure that the item you're trying to make a transaction for has been added this way.
  This can be viewed using the 'View Inventory' button if you happen to forget what items you entered. Additionally, ensure that you are not requesting a transaction for more 
  stock than you provided. The program will alert you if this is attempted. Once a transaction goes through, the cost per item multiplied by stock ordered is added to your 
  store's budget.

  View Inventory:
  Simply switches to a page containing a large text box that contains all stock added via the 'Order Items' button. Each item is numbered in the order they were added to the
  inventory in. You can see each item's name, stock amount, cost for store, and price for customer. If you scroll down to the bottom of this page, the cost for ordering all
  stock is visible as well as the potential profits to be made if the store sells all of its stock.

  Quit:
  Simply closes the GUI window. Run the program again to reopen it, however data entered will not be saved.

  Thank you!
  



