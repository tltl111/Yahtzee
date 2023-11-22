class speler:
    def __init__(self, naam):

        self.naam = naam
        self.scorebord = {}

        self.boven_score = 0
        self.beneden_score = 0
        self.bonus_beneden = 0
        self.totale_score = 0

    def toevoegen_gerold(self, gerold_soort , waarde):
        self.scorebord[gerold_soort] = waarde

    def toevoegen_boven_score(self, waarde):
        self.boven_score += waarde

    def toevoegen_boven_bonus(self):
        benodigde_score_voor_bonus = 63

        if self.pak_boven_score() >= benodigde_score_voor_bonus:
            self.scorebord['boven_bonus'] = 50
        else:
            self.scorebord['boven_bonus'] = 0

        self.boven_bonus = self.scorebord['boven_bonus']

    def pak_boven_score(self):
        return self.boven_score

    def print_scorebord(self):
        for sleutel, waarde in self.scorebord.items():
            print (f'{sleutel} : {waarde}')