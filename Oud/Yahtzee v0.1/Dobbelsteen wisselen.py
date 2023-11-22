import random
from random import randint
import time

def rollen(min, max):
    while True:
        worp1 = input("Wil je de dobbelstenen rollen? (j/n) ")
        if worp1 == "j":
            print("De dobbelstenen zijn aan het rollen...")
            time.sleep(1)
            gerolde_dobbelstenen1 = []
            getal = random.randint(min, max)
            getal2 = random.randint(min, max)
            getal3 = random.randint(min, max)
            getal4 = random.randint(min, max)
            getal5 = random.randint(min, max)
            gerolde_dobbelstenen1.append(getal)
            gerolde_dobbelstenen1.append(getal2)
            gerolde_dobbelstenen1.append(getal3)
            gerolde_dobbelstenen1.append(getal4)
            gerolde_dobbelstenen1.append(getal5)
            print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen1)
            worp2 = input("Wil je proberen je score te verbeteren? Nog 2 kansen (j/n) ")
            if worp2 == "j":
                gerolde_dobbelstenen2 = wissel(gerolde_dobbelstenen1)
                print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen2[0])
                worp3 = input("Wil je proberen je score te verbeteren? Laatste kans (j/n) ")
                if worp3 == "j":
                    gerolde_dobbelstenen3 = wissel(gerolde_dobbelstenen2[0])
                    print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen3[0])
                    print("GAME OVER")
                    break
                if worp3 == "n":
                    print("GAME OVER")
                    break
            if worp2 == "n":
                print("GAME OVER")
                break
        if worp1 == "n":
            print("GAME OVER")
            break

def wissel(steenlijst):
    valid = True
    wisselsteen = input("Type de positie van de stenen die je wilt wissel: (1-5): ")
    wisselsteen = wisselsteen.replace(",", "")
    wisselsteen = wisselsteen.replace(" ", "")
    wisselsteenlijst = []
    for x in wisselsteen:
        wisselsteenlijst.append(x)
    for x in wisselsteenlijst:
        x = str(x)
        if x.isdigit():
            x = int(x)
            if x in range(1, 6):
                valid = True
            else:
                valid = False
        else:
            valid = False

    wisselindex = []

    for x in wisselsteenlijst:
        wisselindex.append(int(x) - 1)

    for x in wisselindex:
        x = int(x)
        x -= 1

    for x in wisselindex:
        steenlijst.pop(x)
        steenlijst.insert(x, randint(1, 6))

    return steenlijst, wisselsteenlijst

rollen(1, 6)