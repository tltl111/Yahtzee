import random
from random import randint
import time
space = 60

def rollen(min, max):
    while True:
        worp1 = input("Wil je de dobbelstenen rollen? (j/n) ")
        if worp1 == "j":
            print("")
            print("De dobbelstenen zijn aan het rollen...")
            print("")
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
            time.sleep(1)
            print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen1)
            worp2 = input("Wil je proberen je score te verbeteren? Nog 2 kansen (j/n) ")
            if worp2 == "j":
                gerolde_dobbelstenen2 = wissel(gerolde_dobbelstenen1)
                print("")
                print("De dobbelstenen zijn aan het rollen...")
                print("")
                time.sleep(1)
                print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen2[0])
                worp3 = input("Wil je proberen je score te verbeteren? Laatste kans (j/n) ")
                if worp3 == "j":
                    gerolde_dobbelstenen3 = wissel(gerolde_dobbelstenen2[0])
                    print("")
                    print("De dobbelstenen zijn aan het rollen...")
                    print("")
                    time.sleep(1)
                    print(format("Je hebt gegooid: ", '60s'), gerolde_dobbelstenen3[0])
                    score = uitslag(gerolde_dobbelstenen3[0])
                    break
                if worp3 == "n":
                    score = uitslag(gerolde_dobbelstenen2[0])
                    break
                else:
                    print("")
                    print("Foute invoer")
                    print("")
            if worp2 == "n":
                score = uitslag(gerolde_dobbelstenen1)
            else:
                print("")
                print("Foute invoer")
                print("")
            return score
        if worp1 == "n":
            print("Yahtzee zonder dobbelstenen te gooien?...")
            break
        else:
            print("")
            print("Foute invoer")
            print("")

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

    while valid == False:
        print("")
        print("Foute invoer")
        print("")
        wisselsteen = input(format("Type de positie van de stenen die je wilt wissel: (1-5): "))
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

def uitslag(steenlijst):
    stenen = []
    for x in steenlijst:
        stenen.append(steenlijst.count(x))
    steenlijstnieuw = sorted(steenlijst)
    steenlijstnieuw = list(set(steenlijstnieuw))
    yahtzee = False
    grote_straat = False
    kleine_straat = False
    full_house = False
    vier_dezelfde = False
    drie_dezelfde = False

    if 5 in stenen:
        yahtzee = True
        print(" " * space, "Yahtzee")
    elif 3 in stenen and 2 in stenen:
        full_house = True
        print(" " * space, "Full house")
    elif 3 in stenen and 2 not in stenen:
        drie_dezelfde = True
        print(" " * space, "Drie dezelfde",)
    elif 4 in stenen:
        vier_dezelfde = True
        print(" " * space, "Vier dezelfde")
    elif len(steenlijstnieuw) == 3:
        print(" " * space, "Niets speciaals")
    elif len(steenlijstnieuw) == 4:
        if steenlijstnieuw[-2] == steenlijstnieuw[-1] - 1 and steenlijstnieuw[-3] == steenlijstnieuw[-2] - 1 and steenlijstnieuw[-4] == \
                steenlijstnieuw[-3] - 1:
            kleine_straat = True
            print(" " * space, "Kleine straat",)
        else:
            print(" " * space, "Niets speciaals")
    elif len(steenlijstnieuw) == 5:
        if steenlijstnieuw[-2] == steenlijstnieuw[-1] - 1 and steenlijstnieuw[-3] == steenlijstnieuw[-2] - 1 and steenlijstnieuw[-4] == \
                steenlijstnieuw[-3] - 1 and steenlijstnieuw[-5] == steenlijstnieuw[-4] - 1:
            grote_straat = True
            print(" " * space, "Grote straat")
        elif steenlijstnieuw[-2] == steenlijstnieuw[-1] - 1 and steenlijstnieuw[-3] == steenlijstnieuw[-2] - 1 and steenlijstnieuw[-4] == \
                steenlijstnieuw[-3] - 1:
            kleine_straat = True
            print(" " * space, "Kleine straat")
        elif steenlijstnieuw[-3] == steenlijstnieuw[-2] - 1 and steenlijstnieuw[-4] == steenlijstnieuw[-3] - 1 and steenlijstnieuw[-5] == \
                steenlijstnieuw[-4] - 1:
            kleine_straat = True
            print(" " * space, "Kleine straat",)
        else:
            print(" " * space, "Niets speciaals")
    else:
        pass

rollen(1, 6)

#yahtzee .........check
#hoge_straat .....check
#lage_straat .....check
#full_house ......check
#vier_dezelfde ...check
#drie_dezelfde ...check
#joker ...........check
#kan nog even niet bededenken hoe ik op bovenstaande wijze de onderstaande worpen kan herkennen...
#aantal_zes
#aantal_vijf
#aantal_vier
#aantal_drie
#aantal_twee
#aantal_een