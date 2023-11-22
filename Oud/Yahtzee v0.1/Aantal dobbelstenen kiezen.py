import random
import time

def rollen(min, max):
    while True:
        aantal_dobbelstenen = int(input("Hoeveel dobbelstenen wil je gooien?"))
        if aantal_dobbelstenen == 1:
            print("De dobbelsteen is aan het rollen...")
            time.sleep(2)
            gerolde_dobbelstenen = []
            getal = random.randint(min, max)
            gerolde_dobbelstenen.append(getal)
            print(f"Jouw getal is {gerolde_dobbelstenen}")
        if aantal_dobbelstenen == 2:
            print("De dobbelstenen zijn aan het rollen...")
            time.sleep(2)
            gerolde_dobbelstenen = []
            getal = random.randint(min, max)
            getal2 = random.randint(min, max)
            gerolde_dobbelstenen.append(getal)
            gerolde_dobbelstenen.append(getal2)
            print(f"Jouw getallen zijn {gerolde_dobbelstenen}")
        if aantal_dobbelstenen == 3:
            print("De dobbelstenen zijn aan het rollen...")
            time.sleep(2)
            gerolde_dobbelstenen = []
            getal = random.randint(min, max)
            getal2 = random.randint(min, max)
            getal3 = random.randint(min, max)
            gerolde_dobbelstenen.append(getal)
            gerolde_dobbelstenen.append(getal2)
            gerolde_dobbelstenen.append(getal3)
            print(f"Jouw getallen zijn {gerolde_dobbelstenen}")
        if aantal_dobbelstenen == 4:
            print("De dobbelstenen zijn aan het rollen...")
            time.sleep(2)
            gerolde_dobbelstenen = []
            getal = random.randint(min, max)
            getal2 = random.randint(min, max)
            getal3 = random.randint(min, max)
            getal4 = random.randint(min, max)
            gerolde_dobbelstenen.append(getal)
            gerolde_dobbelstenen.append(getal2)
            gerolde_dobbelstenen.append(getal3)
            gerolde_dobbelstenen.append(getal4)
            print(f"Jouw getallen zijn {gerolde_dobbelstenen}")
        if aantal_dobbelstenen == 5:
            print("De dobbelstenen zijn aan het rollen...")
            time.sleep(2)
            gerolde_dobbelstenen = []
            getal = random.randint(min, max)
            getal2 = random.randint(min, max)
            getal3 = random.randint(min, max)
            getal4 = random.randint(min, max)
            getal5 = random.randint(min, max)
            gerolde_dobbelstenen.append(getal)
            gerolde_dobbelstenen.append(getal2)
            gerolde_dobbelstenen.append(getal3)
            gerolde_dobbelstenen.append(getal4)
            gerolde_dobbelstenen.append(getal5)
            print(f"Jouw getallen zijn {gerolde_dobbelstenen}")

rollen(1, 6)