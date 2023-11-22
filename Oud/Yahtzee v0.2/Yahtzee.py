from Speler import speler
from Rollen import rollen
import time

def main():

    spel_list_boven = ['eenen' , 'tweeen' , 'drieen' , 'vieren' , 'vijven' , 'zessen']
    spel_list_boven_waardes = [1,2,3,4,5,6]

    speler1 = speler('Tom')
    worp1 = rollen()

    for index,item in enumerate(spel_list_boven):

        print ('-'*40)
        print (f'rollen voor {item}')
        print ('-'*40)

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print (f'Jouw dobbelstenen: {laatste_worp_verzameling}')


        check_score = worp1.enkele_waarde(laatste_worp_verzameling, spel_list_boven_waardes[index] )

        speler1.toevoegen_gerold(item , check_score)
        speler1.toevoegen_boven_score(check_score)

    speler1.toevoegen_boven_bonus()

    speler1.print_scorebord()

main()