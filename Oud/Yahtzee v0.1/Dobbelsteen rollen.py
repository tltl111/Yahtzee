import random

def rollen(min, max):
    while True:
        print("De dobbelsteen is aan het rollen...")
        print(f"Jouw getal is {random.randint(min, max)}")
        answer = input ("wil je nog eens rollen)? (j/n)")
        if answer.lower() == "n":
            break

rollen(1, 6)