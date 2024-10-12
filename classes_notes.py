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
@@ -19,10 +23,7 @@ def fight(self,other):
            other.losses += 1
            self.losses += 1
            return "Tie"
    #use __str__ to print something so we know it does something
    #makes it more readble
    def __str__(self):
        return f"Name: {self.name}\nAge:{self.age}\nSpecies: {self.species}\nGender:{self.gender}\nRarity:{self.rarity}"
    
#we genrally store objects in variles (indivisualy or in a list)so we ca use it
cat = Animal("Tom","cat", 21,"Male","Comomn")
frog = Animal ("Jarrod","Poison Dart Frog","500","Female","Rare")
