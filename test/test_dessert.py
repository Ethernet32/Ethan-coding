from Dessrt_shop_folder.dessert import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_DessertItem():
    testdessertitem = DessertItem("chocolate")
    assert testdessertitem.name == "chocolate"
    assert testdessertitem.name != "amoung us"
    assert testdessertitem.name != "tootsie roll"

def test_Candy():
    testcandy = Candy("snickers",3.5,1.60)
    assert testcandy.name == "snickers"
    assert testcandy.candy_weight == 3.5
    assert testcandy.price_per_pound == 1.60

def test_Cookie():
    testcookie = Cookie("snickerdoodle",6,1.20)
    assert testcookie.name == "snickerdoodle"
    assert testcookie.cookie_quantity == 6
    assert testcookie.price_per_dozen == 1.20

def test_IceCream():
    testicecream = IceCream("green", 3, 4.53)
    assert testicecream.name == "green"
    assert testicecream.scoop_count == 3
    assert testicecream.price_per_scoop == 4.53

def test_Sundae():
    testsundae = Sundae("banana split", 3, 4.53,"Green bits", 0.1)
    assert testsundae.name == "banana split"
    assert testsundae.scoop_count == 3
    assert testsundae.price_per_scoop == 4.53
    assert testsundae.topping_name == "Green bits"
    assert testsundae.topping_price == 0.1