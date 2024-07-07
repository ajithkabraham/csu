class Pizza:
    # constructor function    
    def __init__(self, pizza_size = '12', pizza_type = 'pepperoni', pizza_qty = 1 ):
        self.pizza_size  = pizza_size,
        self.pizza_type = pizza_type,
        self.pizza_qty = pizza_qty

    __ingred_list_cheese = ['dough','sauce','mozzarella','Cheddar', 'Havarti', 'Provolone']
    __ingred_list_meat = ['dough','sauce','mozzarella','sausage', 'beef', 'bacon']
    __ingred_list_pepperoni = ['dough','sauce','Provolone','pepperoni']

    # function to make pizza
    def make_pizza(self):
        ingredients_list = self.__ingred_list_pepperoni[:]
        if self.pizza_type[0] == 'cheese':
            ingredients_list = self.__ingred_list_cheese[:]
        elif self.pizza_type[0] == 'meatlovers':
            ingredients_list = self.__ingred_list_meat[:]
        else:
            print("Invalid pizza")
	
        print('1. Flatten the dough to size,self.pizza_size')
        print('2. Add sauce on pizza')
        print('3. Add ingredients')
        print("\n".join('%s'%item for item in ingredients_list))
        print('4. Bake at 750 degrees(F) for 5 mins')

cheese_pizza1 = Pizza('14','meatlovers',1)
cheese_pizza1.make_pizza()