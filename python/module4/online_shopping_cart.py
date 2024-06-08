# Class Item to purchase
class ItemToPurchase:

    # constructor function    
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0 ):
        self.item_name = item_name,
        self.item_price = item_price,
        self.item_quantity = item_quantity
    # function to print the total cost
    def print_item_cost(self):
        print(self.item_name[0],' ', self.item_quantity, " @ $", self.item_price[0], " = $", (self.item_quantity * self.item_price[0]),sep='' )

# Gather details for first item
print("Item 1")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))
item1 = ItemToPurchase(item_name, item_price,item_quantity)

# Gather details for second item
print("Item 2")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))
item2 = ItemToPurchase(item_name, item_price,item_quantity)

# Print the item details
item1.print_item_cost()
item2.print_item_cost()