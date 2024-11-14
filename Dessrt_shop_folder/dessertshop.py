from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)
from receipt import *

class Order():
    def __init__(self):
        self.order=[]

    def add(self,other):
        self.order.append(other)

    def order_cost(self):
        total = 0.0
        for dessert in self.order:
            total+= dessert.calculate_cost()
        return total
    
    def order_tax(self):
        total = self.order_cost()
        return total*(self.tax_percent/100)


def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    order1.add(Candy("Gummy Bears", .25, .35))
    order1.add( Cookie("Chocolate Chip", 6, 3.99))
    order1.add(IceCream("Pistachio", 2, .79))
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))
    total_item = 0
    for item in order1.order:
        print(item)
        total_item += 1
    print(f"Total number of items in order: {total_item}")
        DATA = [ 
        [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
        [ 
            "16/11/2020", 
            "Full Stack Development with React & Node JS - Live", 
            "Lifetime", 
            "10,999.00/-", 
        ], 
        [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
        [ "Sub Total", "", "", "20,9998.00/-"], 
        [ "Discount", "", "", "-3,000.00/-"], 
        [ "Total", "", "", "17,998.00/-"], 
    ]
    make_receipt(DATA,"reciept.pdf")
main()
