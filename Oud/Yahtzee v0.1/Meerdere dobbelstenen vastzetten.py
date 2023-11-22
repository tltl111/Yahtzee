import random

def rollen(min, max):
    while True:
        print("De dobbelsteen is aan het rollen...")
        gerolde_dobbelstenen = []
        getal = random.randint(min, max)
        gerolde_dobbelstenen.append(getal)
        print(f"Jouw getal is {gerolde_dobbelstenen}")
        answer = input("wil je nog eens rollen? (j/n)")
        if answer.lower() == "n":
            break
        if answer.lower() == "j":
            print("De dobbelsteen is aan het rollen...")
            getal2 = random.randint(min, max)
            gerolde_dobbelstenen.append(getal2)
            print(f"Jouw getallen zijn {gerolde_dobbelstenen}")
            answer = input("wil je nog eens rollen? (j/n)")
            if answer.lower() == "n":
                break
            if answer.lower() == "j":
                print("De dobbelsteen is aan het rollen...")
                getal3 = random.randint(min, max)
                gerolde_dobbelstenen.append(getal3)
                print(f"Jouw getallen zijn {gerolde_dobbelstenen}")
                answer = input("Wil je opnieuw beginnen? (j/n)")
                if answer.lower() == "n":
                    break

rollen(1, 6)