price="$",0

class Order:
    def __init__(self, drink=None, appetizer=None, main=None, side1=None, side2=None, dessert=None):
        self.drink=drink
        self.appetizer=appetizer
        self.main=main
        self.side1=side1
        self.side2=side2
        self.dessert=dessert
    def __str__(self):
        return f"Drink: {self.drink}\nAppetizer: {self.appetizer}\nMain Course: {self.main}\nSide One: {self.side1}\nSide Two: {self.side2}\nDessert: {self.dessert}"
    @classmethod
    def ordering(self):
        order=input("What would you like to order\na. Drink\nb. Appetizer\nc. Main Course\nd. Side One\ne. Side Two\nf. Dessert\n")
        if order == "a":
            see_menu=input("Would you like o see a menu before you order(y/n)\n")
            if see_menu=="y":
                for i in drink_menu:
                    print(f"{i}. {drink_menu[i]}")
            drink_choice=input("What drink Do you want\n")
            if int(drink_choice) in drink_menu:
                return f"{drink_menu[int(drink_choice)]} is {drink_prices.get(int(drink_choice))}"
            else:
                return f"Invalid response"


drink_menu={1:"Coke",2:"Milk"}
drink_prices={1:1.25}
appetizer_menu={}
main_menu={}
side_menu={}
dessert_menu={}
order1=Order()
print(order1.ordering())
