price=0.0
print("\033c")
class Order:
    def __init__(self, drink, appetizer, main, side1, side2, dessert):
        self.drink=drink
        self.appetizer=appetizer
        self.main=main
        self.side1=side1
        self.side2=side2
        self.dessert=dessert
    def __str__(self):
        return f"Drink: {self.drink}\nAppetizer: {self.appetizer}\nMain Course: {self.main}\nSide One: {self.side1}\nSide Two: {self.side2}\nDessert: {self.dessert}"
    def ordering(self):
        global price
        order=input("What would you like to order\na. Drink\nb. Appetizer\nc. Main Course\nd. Side One\ne. Side Two\nf. Dessert\n")
        if order == "a":
            print("\033c")
            see_menu=input("Would you like to see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=drink_menu.keys()
                for k in mm:
                    print(k)
            drink_choice=input("What drink Do you want\n")
            drink_choice.strip()
            drink_choice.lower()
            print("\033c")
            if drink_choice in drink_menu:
                print("\033c")
                self.drink=drink_choice
                price = price + drink_menu[drink_choice]
                return f"{drink_choice} is {drink_menu[drink_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
        elif order == "b":
            print("\033c")
            see_menu=input("Would you like to see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=appetizer_menu.keys()
                for k in mm:
                    print(k)
            appetizer_choice=input("What appetizer Do you want\n")
            appetizer_choice.strip()
            appetizer_choice.lower()
            print("\033c")
            if appetizer_choice in appetizer_menu:
                print("\033c")
                price = price + appetizer_menu[appetizer_choice]
                self.appetizer=appetizer_choice
                return f"{appetizer_choice} is {appetizer_menu[appetizer_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
        elif order == "c":
            print("\033c")
            see_menu=input("Would you like to see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=main_menu.keys()
                for k in mm:
                    print(k)
            main_choice=input("What maincousre Do you want\n")
            main_choice.strip()
            main_choice.lower()
            print("\033c")
            if main_choice in main_menu:
                print("\033c")
                price = price + main_menu[main_choice]
                self.main=main_choice
                return f"{main_choice} is {main_menu[main_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
        elif order == "d":
            print("\033c")
            see_menu=input("Would you like to see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=side_menu.keys()
                for k in mm:
                    print(k)
            side_choice=input("What side Do you want\n")
            side_choice.strip()
            side_choice.lower()
            print("\033c")
            if side_choice in side_menu:
                print("\033c")
                price = price + side_menu[side_choice]
                self.side1=side_choice
                return f"{side_choice} is {side_menu[side_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
        elif order == "e":
            print("\033c")
            see_menu=input("Would you like o see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=side_menu.keys()
                for k in mm:
                    print(k)
            side_choice=input("What side Do you want\n")
            side_choice.strip()
            side_choice.lower()
            print("\033c")
            if side_choice in side_menu:
                print("\033c")
                price = price + side_menu[side_choice]
                self.side2=side_choice
                return f"{side_choice} is {side_menu[side_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
        if order == "f":
            print("\033c")
            see_menu=input("Would you like to see a menu before you order(y/n)\n")
            print("\033c")
            if see_menu=="y":
                mm=dessert_menu.keys()
                for k in mm:
                    print(k)
            dessert_choice=input("What drink Do you want\n")
            dessert_choice.strip()
            dessert_choice.lower()
            print("\033c")
            if dessert_choice in dessert_menu:
                print("\033c")
                price = price + dessert_menu[dessert_choice]
                self.dessert=dessert_choice
                return f"{dessert_choice} is {dessert_menu[dessert_choice]}\nYour total is ${price:.2f}"
            else:
                print("\033c")
                return f"That is not on the menu sorry"
    def check_out(self):
        if self.drink != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        elif self.appetizer != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        elif self.main != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        elif self.side1 != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        elif self.side2 != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        elif self.dessert != None:
            return f"Your total comes out to ${price:.2f}\nThank you for shopping at Wendy's{quit()}"
        else:
            return f"You need to order something"

drink_menu={"coke":1.21,"milk":3.51,"mustard":0.51,"Pepsi":3.71}
appetizer_menu={"bruschetta":10.01,"bread":1.01,"chips":2.51,"guacamole":0.21}
main_menu={"hamburger":17.11,"pizza":9.76,"lobster":50.32}
side_menu={"fries":3.61,"sushi":6.51,"chicken_nuggets":9.52}
dessert_menu={"icecream":4.01,"sugar":9.46,"chaco_taco":99.53}
order=Order(None, None, None, None, None, None)

start=input("would you like place your order(y/n)")
if start == "y":
    while True:
        print(order.ordering())
        see_order=input("woul you like to see your order(y/n)")
        check_out=input("would you like to check out(y/n)")
        if check_out == "y":
            print(order.check_out())
            break
        print("\033c")
