class speler:
    def __init__(self, naam):

        self.naam = naam
        self.scorebord = {}

        self.enkele_score = 0
        self.speciale_score = 0
        self.bonus_speciale = 0
        self.totale_score = 0

    def toevoegen_gerold(self, gerold_soort, waarde):
        self.scorebord[gerold_soort] = waarde

    def toevoegen_enkele_score(self, waarde):
        self.enkele_score += waarde

    def toevoegen_speciale_score(self, waarde):
        self.speciale_score += waarde

    def toevoegen_totale_score(self, waarde):
        self.totale_score += waarde

    def toevoegen_naam(self):
        self.scorebord['Naam'] = self.pak_naam()

    def toevoegen_enkele_score_totaal(self):
        if self.pak_enkele_score() >= 0:
            self.scorebord['Totaal boven'] = self.pak_enkele_score()
        if self.pak_enkele_score() == 0:
            self.scorebord['Totaal boven'] = 0

    def toevoegen_speciale_score_totaal(self):
        if self.pak_speciale_score() >= 0:
            self.scorebord['Totaal onder'] = self.pak_speciale_score()
        if self.pak_speciale_score() == 0:
            self.scorebord['Totaal onder'] = 0

    def toevoegen_score_totaal(self):
        self.scorebord['Totaal'] = self.pak_totale_score()

    def toevoegen_enkele_bonus(self):
        benodigde_score_voor_bonus = 63
        if self.pak_enkele_score() >= benodigde_score_voor_bonus:
            self.scorebord['Bonus'] = 35
        else:
            self.scorebord['Bonus'] = 0
        self.enkele_bonus = self.scorebord['Bonus']

    def pak_enkele_score(self):
        return self.enkele_score

    def pak_speciale_score(self):
        return self.speciale_score

    def pak_totale_score(self):
        return self.totale_score

    def pak_naam(self):
        return self.naam

    def print_scorebord(self):
        for sleutel, waarde in self.scorebord.items():
            print(f'{sleutel} : {waarde}')
