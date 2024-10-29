class PetStore:
    name = "Pet Smart"

    def __init__(self, id_number):
        self.id_number= id_number
        self.animals = []
        self.featured_pet = None
    
    def add_pet(self, animal):
        #assert will check i statement is true and stop code is false
        #isinstance is lik isnum and just checks if it is an instance
        assert isinstance(animal,Animal)
        self.animals.append(animal)

    def remove_pet(self,animal):
        try:
            self.animals.remove(animal)
        except:
            print("no such animal")
        else:
            print(animal, "removeed")
        
    def feature(self,name):
        for pet in self.animals:
            if pet.name == name:
                print("Feature pet", pet)
                break
        else:
            print("no such animal")

    def get_featured(self):
        return self.featured_pet

    def feed(self):
        for pet in self.animals:
            pet.eat()
    def get_mammals(self):
        return self.get_by_type(Mammal)

    def get_reptiles(self):
        return self.get_by_type(Reptile)

    def get_anphibian(self):
        return self.get_by_type(Anphibian)

    def get_fish(self):
        return self.get_by_type(Fish)

    def get_by_type(self, typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]

class Animal:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"This is {self.name}"

    def eat(self):
        print(f"{self.name} Eating {self.diet}")

class Mammal(Animal):
    pass


class Cat(Mammal):
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"

class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodent"

class Turle(Reptile):
    diet = "letuce"

class Birds(Animal):
    pass

class Toucan(Birds):
    diet = "caterpilars"

class Paracete(Birds):
    diet = "seeds"

class Anphibian(Animal):
    pass

class Frog(Anphibian):
    diet = "flys"

class Newt(Anphibian):
    diet = "worms"

class Fish(Animal):
    pass
class Coy(Fish):
    diet = "algee"

class GoldFish(Fish):
    diet = "pellot"

store= PetStore(1)
store.add_pet(Turle("straw"))
store.add_pet(Cat("Joe"))
store.add_pet(Turle("Flash"))
store.add_pet(Snake("Robin"))

store.feature("Flash")
store.feed()

print("Repiles: ")
for pet in store.get_fish():
    print(pet)