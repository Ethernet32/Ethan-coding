#we start with keyword class and we name them usinf PascalCase
class Animal:
    #we start wih the constructor
    #use __str__ to print something so we know it does something
    #makes it more readble
    def __str__(self):
        return f"Name: {self.name}\nAge:{self.age}\nSpecies: {self.species}\nGender:{self.gender}\nRarity:{self.rarity}"
    def __init__(self,name, species,age,gender,rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
    #methods are funstions in class
    def fight(self,other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name+"won the fight"
        elif len(self.name) < len(other.name):
            self.losses += 1
            return other.name+"won the fight"
        else:
            other.losses += 1
            self.losses += 1
            return "Tie"
    
#we genrally store objects in variles (indivisualy or in a list)so we ca use it
cat = Animal("Tom","cat", 21,"Male","Comomn")
frog = Animal ("Jarrod","Poison Dart Frog","500","Female","Rare")
print(cat)
print(frog)
#to call a method you put the name of the object.name of the method (needed arguments)
cat.losses=0
frog.losses=0
print(cat.fight(frog))

cat.name="Thomas"
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print(cat)