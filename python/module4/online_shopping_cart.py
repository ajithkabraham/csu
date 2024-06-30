# Class Item to purchase
class ItemToPurchase:

    # constructor function    
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0 ):
        self.item_name = item_name,
        self.item_price = item_price,
        self.item_quantity = item_quantity
    # function to print the total cost
    def print_item_cost(self):
        print(self.item_name[0],' ', self.item_quantity, " @ $", self.item_price[0], ' = ${:.2f}'.format(self.item_quantity * self.item_price[0]),sep='' )
        return (self.item_quantity * self.item_price[0])

class ShoppingCart:
    cart_items = []
    # constructor function    
    def __init__(self, cust_name = 'none', date = 'January 1, 2020' ):
        self.cust_name = cust_name,
        self.date = date
    

    def add_item(self,itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
        else:
            print(" Item not found in cart")

    def modify_item(self, itemToPurchase):
        if itemToPurchase.item_name in self.cart_items:
            if itemToPurchase.item_price == 0 or itemToPurchase.item_quantity == 0:
                #modify
                itemToPurchase.item_price = 0
            else:
                print("Item not found in cart")
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price[0] * item.item_quantity)
        return total_cost
    def print_total(self,itemToPurchase):
        total_cost = self.get_cost_of_cart()
        if (total_cost > 0):
            print("Total price: ", total_cost)
        else:
            print("SHOPPING CART IS EMPTY")
    def print_descriptions(self):
        print(self.cust_name)
        
# Main code
# Gather details for first item
print("Item 1")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))
item1 = ItemToPurchase(item_name, item_price,item_quantity)
#item1 = ItemToPurchase('Chips', 2,10)

# Gather details for second item
print("Item 2")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))
item2 = ItemToPurchase(item_name, item_price,item_quantity)
#item2 = ItemToPurchase('headphones', 3,40)

# Print the item details
print('TOTAL COST')
item1_total = item1.print_item_cost()
item2_total = item2.print_item_cost()
print('Total: ${:.2f}'.format(item1_total + item2_total))

shoppingCart1 = ShoppingCart('John Doe', 'June 16, 2024')
print(shoppingCart1.cust_name)
shoppingCart1.add_item(item1)
shoppingCart1.add_item(item2)
print(shoppingCart1.get_num_items_in_cart())
#shoppingCart1.remove_item(item1)
#print(shoppingCart1.get_num_items_in_cart())
print(shoppingCart1.get_cost_of_cart())


def print_menu():
    print('MENU\n')
    print('a - Add item to cart\n')
    print('r - Remove item from cart\n')
    print('c - Change item quantity\n')
    print("i - Output items' descriptions'\n")
    print('o - Output shopping cart\n')
    print('q - Quit\n')
    print('Choose an option:\n')
    menu_input = input()
    return menu_input
def print_output():
    print('OUTPUT SHOPPING CART')
    print(shoppingCart1.cust_name[0], '\'s Shopping Cart - ', shoppingCart1.date)
    print('Number of Items: ',shoppingCart1.get_num_items_in_cart())
    for item_name in shoppingCart1.cart_items:
        item_name.print_item_cost()
    print('Total: ${:.2f}'.format(shoppingCart1.get_cost_of_cart()))


menu_input = print_menu()
if menu_input == 'q':
    print('quit')
elif menu_input == 'a':
    print('add new items')
elif menu_input == 'r':
    print('remove items')
elif menu_input == 'i':
    print('get descriptions')
elif menu_input == 'o':
    print_output()
else:
    print('Please enter a valid choice from the menu\n')
    print_menu()

