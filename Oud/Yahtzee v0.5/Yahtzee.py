from Speler import speler
from Rollen import rollen


def main():

    spel_list_enkele = ['Eeen', 'Tween', 'Drieën', 'Vieren', 'Vijven', 'Zessen']
    spel_list_enkele_waardes = [1, 2, 3, 4, 5, 6]
    spel_list_yahtzee = ['Yahtzee']
    spel_list_grote_straat = ['Grote straat']
    spel_list_kleine_straat = ['Kleine straat']
    spel_list_full_house = ['Full house']
    spel_list_vier_dezelfde = ['Vier dezelfde']
    spel_list_drie_dezelfde = ['Drie dezelfde']

    spelernaam1 = input('Naam speler 1? ')
    spelernaam2 = input('Naam speler 2? ')
    speler1 = speler(spelernaam1)
    speler1.toevoegen_naam()
    speler2 = speler(spelernaam2)
    speler2.toevoegen_naam()

    worp1 = rollen()

    for index, item in enumerate(spel_list_enkele):

        print('-'*40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-'*40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.enkele_waarde(laatste_worp_verzameling, spel_list_enkele_waardes[index])

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_enkele_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    speler1.toevoegen_enkele_bonus()
    speler1.print_scorebord()

    for index, item in enumerate(spel_list_enkele):

        print('-'*40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-'*40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.enkele_waarde(laatste_worp_verzameling, spel_list_enkele_waardes[index])

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_enkele_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    speler2.toevoegen_enkele_bonus()
    speler2.print_scorebord()

    for index, item in enumerate(spel_list_yahtzee):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_yahtzee(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_yahtzee):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_yahtzee(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_grote_straat):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_grote_straat(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_grote_straat):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_grote_straat(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_kleine_straat):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_kleine_straat(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_kleine_straat):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_kleine_straat(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_full_house):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_full_house(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_full_house):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_full_house(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_vier_dezelfde):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_vier_dezelfde(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_vier_dezelfde):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_vier_dezelfde(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_drie_dezelfde):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam1))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_drie_dezelfde(laatste_worp_verzameling)

        speler1.toevoegen_gerold(item, check_score)
        speler1.toevoegen_speciale_score(check_score)
        speler1.toevoegen_totale_score(check_score)

    for index, item in enumerate(spel_list_drie_dezelfde):

        print('-' * 40)
        print(f'rollen voor {item} :', (spelernaam2))
        print('-' * 40)
        print('')

        worp1.rollen_stenen()
        bewaar1 = worp1.bewaar_stenen()

        worp1.opnieuw_rollen_stenen(bewaar1)
        bewaar2 = worp1.bewaar_stenen()

        worp3 = worp1.opnieuw_rollen_stenen(bewaar2)
        worp1.gedwongen_bewaren(worp3)

        laatste_worp_verzameling = worp1.pak_huidige_bewaar_stenen()

        print(f'Jouw dobbelstenen: {laatste_worp_verzameling}')
        print('')

        check_score = worp1.check_drie_dezelfde(laatste_worp_verzameling)

        speler2.toevoegen_gerold(item, check_score)
        speler2.toevoegen_speciale_score(check_score)
        speler2.toevoegen_totale_score(check_score)

    speler1.toevoegen_enkele_score_totaal()
    speler1.toevoegen_speciale_score_totaal()
    speler1.toevoegen_score_totaal()
    speler2.toevoegen_enkele_score_totaal()
    speler2.toevoegen_speciale_score_totaal()
    speler2.toevoegen_score_totaal()
    speler1.print_scorebord()
    print('-' * 40)
    speler2.print_scorebord()


main()
