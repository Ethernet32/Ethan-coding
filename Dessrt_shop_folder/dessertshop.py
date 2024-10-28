from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

class Order():
    def __init__(self):
        self.order=[]


    def add(self,other):
        self.order.append(other)

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
main()