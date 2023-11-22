from random import randint

def roll_dice():
    print(f"Numbers is : {randint(1,6)}")

roll_dice()

whatever = int(input("How many dice do you want to roll?"))

for number in range(whatever):
    roll_dice()