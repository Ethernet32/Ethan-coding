from dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_Candy():
    testcandy = Candy("snickers",3.5,1.60)
    assert testcandy.name == "snickers"
    assert testcandy.candy_weight == 3.5
    assert testcandy.price_per_pound == 1.60

def test_Cookie():
    testcookie = Cookie("snickerdoodle",6,1.20)
    assert testcookie.name == "snickerdoodle"