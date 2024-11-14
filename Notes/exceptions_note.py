#help fix problem that arise during user mess ups
#the computer looks for zero ivision, file not found, value error, type error, index eror
while True:
    try:
        num = int(input("tell me a number: "))
    except ValueError:
        print("wasnt a whole number")
    else:
        break
while True:
    try:
        numtwo = int(input("tell me another number: "))
    except ValueError:
        print("wasnt a whole number")
        continue
    else:
        try:
            print(f"{str(num)} divided {numtwo} equals {num / numtwo}")
            break
        except ZeroDivisionError:
            print("You can't divide by 0, try again")
            continue
    finally:
        print("this willl always happen")
    #raise:
    #this rasies an error like to stop user form entering the number 7