from datetime import datetime

# Class Item to purchase
class ItemToPurchase:
    count = 0

    # constructor function    
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = '' ):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        ItemToPurchase.count += 1
    # function to print the total cost
    def print_item_cost(self):
        print(self.item_name,' ', self.item_quantity, " @ $", self.item_price, ' = ${:.2f}'.format(self.item_quantity * self.item_price),sep='' )
        return (self.item_quantity * self.item_price)

class ShoppingCart:
    cart_items = []
    count = 0 
    # constructor function    
    def __init__(self, cust_name = 'none', date = 'January 1, 2020' ):
        self.cust_name = cust_name
        self.date = date
        ShoppingCart.count += 1
    

    def add_item(self,itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
        else:
            print(" Item not found in cart")

    def modify_item(self, itemToPurchase):
        print('To modify quantity, press q')
        print('To modify description, press d')
        print('To modify price, press p\n')
        type_to_modify = input()
        if type_to_modify == 'q':
            new_qty = int(input('Enter new quantity\n'))
            itemToPurchase.item_quantity = new_qty
        elif type_to_modify == 'd':
            new_desc = input('Enter new description\n')
            itemToPurchase.item_description = new_desc
        elif type_to_modify == 'p':
            new_price = float(input('Enter the new price\n'))
            itemToPurchase.item_price = new_price
            print( itemToPurchase.item_price)
        else:
            print("Invalid input")
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)
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
    print(shoppingCart.cust_name, '\'s Shopping Cart - ', shoppingCart.date)
    print('Number of Items: ',shoppingCart.get_num_items_in_cart())
    for item_name in shoppingCart.cart_items:
        item_name.print_item_cost()
    print('Total: ${:.2f}'.format(shoppingCart.get_cost_of_cart()))
def print_description():
    print('OUTPUT ITEMS\' DESCRIPTIONS')
    print(shoppingCart.cust_name, '\'s Shopping Cart - ', shoppingCart.date)
    print('Item Descriptions')
    for item in shoppingCart.cart_items:
        print(item.item_name,':',item.item_description)
items_list = []
while True:
    menu_input = print_menu()
    if menu_input == 'q':
        break
    elif menu_input == 'a':
        items_in_cart_count = ItemToPurchase.count
        shopping_carts_count = ShoppingCart.count
        if shopping_carts_count == 0:
            s_cart_name = input("Enter your name:\n")
            s_cart_date = datetime.now().strftime("%B %d, %Y")
            shoppingCart = ShoppingCart(s_cart_name, s_cart_date)
            print('Customer name:',s_cart_name)
            print('Today\'s date:',s_cart_date)
        item_name = input("Enter the item name:\n")
        items_list.append(item_name)
        item_desc = input('Enter the item description\n')
        item_price = float(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        item = ItemToPurchase(item_name, item_price,item_quantity, item_desc)
        shoppingCart.add_item(item)

    elif menu_input == 'r':
        item_to_remove = input("Enter the item to remove:\n")
        if (item_to_remove in items_list):
            for item in shoppingCart.cart_items:
                if item.item_name == item_to_remove:
                    shoppingCart.remove_item(item)
        else:
            print("Item not found in shopping cart.")

    elif menu_input == 'c':
        item_to_modify = input('Enter item to modify\n')
        if (item_to_modify in items_list):
            for item in shoppingCart.cart_items:
                if item.item_name == item_to_modify:
                    shoppingCart.modify_item(item)
        else:
            print("Item not found in shopping cart.")
    elif menu_input == 'i':
        print_description()
    elif menu_input == 'o':
        print_output()
    else:
        print('Please enter a valid choice from the menu\n')

