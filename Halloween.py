class Monster:
    def __init__(self,name,attack,weakness):
        self.name=name
        self.attack=attack
        self.weakness=weakness
    def __str__(self):
        return f"Name: {self.name}\nAttack: {self.attack}\nWeakness: {self.weakness}"
class Necrons(Monster):
    def __init__(self, name, attack, weakness):
        super().__init__(name, attack, weakness)
class Beast_of_nurgle(Monster):
    def __init__(self, name, attack, weakness):
        super().__init__(name, attack, weakness)
class Ork(Monster):
    def __init__(self, name, attack, weakness):
        super().__init__(name, attack, weakness)
class ImperiumOfMan(Monster):
    #because the ture monster is the imperium of man
    def __init__(self, name, attack, weakness):
        super().__init__(name, attack, weakness)

class MonsterList:
    def __init__(self):
        self.list=[]

    def add(self,other):
        self.list.append(other)
def main():
    warhammer = MonsterList()
    warhammer.add(Necrons("Necron","lazer blast","old gods"))
    warhammer.add(Beast_of_nurgle("Beast_of_nurgle","sickness","Soap"))
    warhammer.add(Ork("Ork","blasta","logic"))
    warhammer.add(ImperiumOfMan("Imperium of Man","Space marines","ethics"))
    for item in warhammer.list:
        print(item)
main()
        