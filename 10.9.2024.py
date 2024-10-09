#10/9/2024
class pokemon:
    def __init__(self,name,hp,typ,lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    def combat(self,other):
        print(f"{self.name} is figting {other.name}")
        if self.lvl > other.lvl:
            return f"The winner is {self.name}"
        if self.lvl < other.lvl:
            return f"The winner is {other.name}"
    def __str__(self):
        return (f"""name:{self.name}\ntype: {self.lvl}\nhp: {self.lvl} """)
    
    #@classmethod to keep method from changing object instances
    def lvl_up(self):
        self.lvl += 1
        self.hp == int(self.hp * 1.5)
        return f"{self.name} leveled up"
    @classmethod 
    def pikachu(self):
        return pokemon(input("Give me a name for pikachu "), 50, "Electric", 1)
    #static methods do not require self or class
    def hp_update(poke):
        return poke.hp - 5

pika = pokemon.pikachu()
eevee = pokemon("JayRod",37,"normal",2)

print(pika)

pika.hp = pokemon.hp_update(pika)

print(pika)