import random

def rollen(min, max):
    while True:
        print("De dobbelsteen is aan het rollen...")
        gerolde_dobbelstenen = []
        getal = random.randint(min, max)
        gerolde_dobbelstenen.append(getal)
        print(f"Jouw getallen is {gerolde_dobbelstenen}")
        answer = input ("wil je nog eens rollen)? (j/n)")
        if answer.lower() == "n":
            print(gerolde_dobbelstenen)
            break

rollen(1, 6)