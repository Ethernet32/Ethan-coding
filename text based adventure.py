import time,sys
import turtle 
import random
print("\033c")
def text(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

heart=3
classespassed=0
dp=1

def next():
  print()
  moveon=input("[press enter to continue]")
  if moveon=="": 
    print("\033c")

def start(): 
  print("\033c")
  text("You walk into school to take your finals and pass your teachers' classes to graduate and go to your dream college. You only need to pass three classes to graduate.")
  next()

def g_ending():
  print("\033c")
  text("You passed all your classes, defeated the principle,and graduated with an associate degree from Ucas. You get to get your diploma, graduate with all your friends, got in to our dream college.")
  next()

def b_ending():
  print("\033c")
  text("You failed. You won’t get to college with your friends. You will be stuck at this school for another year.")
  next()
math={1 : "7*8",2 : "5*9",3:"6^2",4:"40/8",5:"2345+890",6:"solve for X: 3x+2=11",7: "5^3",8: "4*12", 9: "360/5", 10: "solve for X:7x+3=17"}
science={1: "What is the atomic number for helium",2: "What is the symbol for Iron on the periodic table",3: "True or false: a plant with out water will die", 4: "Is water lava",5: "What does DNA stand for",6: "True or false sodium reacts violently to water",7: "What is the symbol for soidium on the periodic table",8: "what is the atomic number of Oxygen",9: "How many teeth dohumans have",10: "True or false sound travels faster than light"}
health={1: "What body system does the heart belong to",2: "True or false you can't live with out the resitry system",3: "What food group contains meats and eggs", 4: "how many teeth should a human adult have",5: "True or false You need 8 hours of sleep each night",6: "True or false milk can only come from cows",7: "what food group contain bread",8: "What body system does the small intestine belong to",9: "True or false You don't need 8 hours of sleep each night",10: "What food groups contais milk and icecream"}

math_answer={1 : "56",2 : "45",3:"36",4:"5",5:"3235",6:"3" ,7: "125",8: "48", 9: "72", 10: "2"}
science_answer={1: "2",2: "Fe",3: "true", 4: "yes",5: "Deoxyribonucleic acid",6: "true",7: "Na",8: "8",9: "32",10: "false"}
health_answer={1: "cardiovascular system",2: "true",3: "protein", 4: 32,5: "true",6: "false",7: "grain",8: "digestive system",9: "false",10: "dairy"}
subjet=[ math, science, health]
answers=[math_answer,science_answer,health_answer]

itemlist = {"notebook":0,"whiteout":0,"cellphone":0}
items = ["notebook","whiteout","cellphone"]
def combat(subject,answer,classname,ehealth=3, damage=1):
  global heart
  global classespassed
  global dp
  x=0
  m=""
  ap=random.randint(1,3)
  if ap == 2:
    ehealth=5
    m="AP"

  while True:
    damage=1
    dp=1
    x+=1
    print("\033c")
    print ("Question", x)
    text(subject[x])
    print("")
    text("Would you like to use an item before answering")
    use_item=input("\n")
    if use_item == "yes":
    
      print(items[0])
      print(itemlist["notebook"])
      print(items[1])
      print(itemlist["whiteout"])
      print(items[2])
      print(itemlist['cellphone'])
      use=input("(type the name of the item you what to use)"+"\n")
      if use=="notebook":
        notebook()
        questin=input(subject[x]+"\n")
      elif use=="whiteout":
        whiteout()
      elif use=="cellpone":
        cellphone()
        questin=input(subject[x]+"\n")
      else:
        text("invalid input")
        next()
        questin=input(subject[x]+"\n")
    else:
      questin=input(subject[x]+"\n")
    if str(questin) == answer[x]:
      print("\033c")
      text("You got it right")
      ehealth-=dp
      next()
      if ehealth==0:
        print("\033c")
        print("You passed",m,classname, "class")
        next()
        classespassed+=1
        give_item()
        text("the teacher dropped an item")
        break
    else:
      print("\033c")
      text("You got it wrong")
      print("")
      heart -= damage
      print("you have",heart,"misakes left")
      if heart==0:
        text("you failed")
        next()
        b_ending()
        break
      next()
  
  if classespassed >= 3:
    text("you passed all you classes you neee to go see the princible")

def notebook():
  global heart
  if itemlist["notebook"] > 0: 
    text("you healed one heart")
    heart += 1
    itemlist["notebook"]-=1
    next()
  else:
    text("you don't have this Item")
    next()
def whiteout():
  if itemlist["notebook"] > 0: 
    text("Question Skipped")
    next()
    worked=1
  else:
    text("you don't have this Item")
    next()
    worked=1
  return worked
def cellphone():
  global heart
  global dp
  if itemlist["notebook"] > 0: 
    cell=random.randrange(0,3)
    if cell==1:
      text("you got caught")
      heart -= 1
      print("you have",heart,"misakes left")
      next()
    else:
      text("the teachers din' catch you ")
      dp==2
    next()
  else:
    text("you don't have this Item")
    next()
def give_item():
  item_chance=random.randrange(0,4)
  if item_chance==1:
    itemlist["notebook"]+=1
  elif item_chance==1:
    itemlist["whiteout"]+=1
  elif item_chance==1:
    itemlist["cellphone"]+=1
start()
text ("as you walk up the stair you come across your classes")

combat(science,science_answer, "science")
