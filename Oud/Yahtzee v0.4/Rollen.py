import random


class rollen:

    def __init__(self):
        self.huidige_stenen_list = []
        self.huidige_bewaar_stenen = []

    def rollen_stenen(self):
        self.huidige_bewaar_stenen.clear()
        self.huidige_stenen_list = [random.randint(1, 6) for steen in range(0, 5)]
        print(f'Je hebt gerold: {self.huidige_stenen_list} \n')
        return self.huidige_stenen_list

    def bewaar_stenen(self):
        while True:
            bewaar_invoer = input('Welke dobbelstenen wil je bewaren (scheiden met comma bijv 2,2,6)? ')
            print('')
            if bewaar_invoer == '0':
                return self.huidige_stenen_list
            if bewaar_invoer == '':
                return self.huidige_stenen_list
            if bewaar_invoer.isupper() or bewaar_invoer.islower():
                print('Dobbelstenen kunnen alleen getallen zijn')
                print('')
            else:
                if not bewaar_invoer.isupper() or bewaar_invoer.islower():
                    splits_invoer = bewaar_invoer.split(',')
                    splits_invoer_int = [int(item) for item in splits_invoer]
                    for waarde in splits_invoer_int:
                        if waarde not in self.huidige_stenen_list:
                            print('Je kunt alleen dobbelstenen bewaren die je gerold hebt')
                            print('')
                        else:
                            if waarde in self.huidige_stenen_list:
                                for steen in splits_invoer_int:
                                    self.huidige_bewaar_stenen.append(steen)
                                for waarde in splits_invoer_int:
                                    if waarde in self.huidige_stenen_list:
                                        self.huidige_stenen_list.remove(waarde)
                                return self.huidige_stenen_list

    def opnieuw_rollen_stenen(self, stenen_list):
        self.huidige_stenen_list = [random.randint(1, 6) for steen in range(0, (len(stenen_list)))]
        print(f'Je hebt gegooid: {self.huidige_stenen_list} \n')
        return self.huidige_stenen_list

    def pak_huidige_stenen(self):
        return self.huidige_stenen_list

    def pak_huidige_bewaar_stenen(self):
        return self.huidige_bewaar_stenen

    def gedwongen_bewaren(self, stenen_list):
        for steen in stenen_list:
            self.huidige_bewaar_stenen.append(steen)

    def check_yahtzee(self, stenen_list):
        if len(set(stenen_list)) == 1:
            return 50
        return 0

    def check_grote_straat(self, stenen_list):
        stenen_list.sort()
        if len(set(stenen_list)) == 5 and stenen_list[4] == 6 and stenen_list[0] == 2:
            return 40
        elif len(set(stenen_list)) == 5 and stenen_list[4] == 5 and stenen_list[0] == 1:
            return 40
        return 0

    def check_kleine_straat(self, stenen_list):
        stenen_list.sort()
        if len(set(stenen_list)) == 5 and stenen_list[4] == 6 and stenen_list[0] == 2:
            return 30
        elif len(set(stenen_list)) == 5 and stenen_list[4] == 5 and stenen_list[0] == 1:
            return 30
        elif len(set(stenen_list)) == 4 and stenen_list[4] == 6 and stenen_list[0] == 3:
            return 30
        elif len(set(stenen_list)) == 4 and stenen_list[4] == 5 and stenen_list[0] == 2:
            return 30
        elif len(set(stenen_list)) == 4 and stenen_list[4] == 4 and stenen_list[0] == 1:
            return 30
        return 0

    def check_full_house(self, stenen_list):
        stenen_list.sort()
        if (len(set(stenen_list))) != 2:
            return 0
        elif stenen_list[0] != stenen_list[3] or stenen_list[1] != stenen_list[4]:
            return 25
        return 0

    def check_vier_dezelfde(self, stenen_list):
        vier_score = sum(stenen_list)
        stenen_list.sort()
        if stenen_list[0] == stenen_list[3] or stenen_list[1] == stenen_list[4]:
            return vier_score
        return 0

    def check_drie_dezelfde(self, stenen_list):
        drie_score = sum(stenen_list)
        stenen_list.sort()
        if stenen_list[0] == stenen_list[2] or stenen_list[1] == stenen_list[3] or stenen_list[2] == stenen_list[4]:
            return drie_score
        return 0

    def add_joker(self, stenen_list):
        pass

    def enkele_waarde(self, stenen_list, check_waarde):
        rollen_score = 0
        for steen in stenen_list:
            if steen == check_waarde:
                rollen_score += steen
        return rollen_score


stenen = rollen()
