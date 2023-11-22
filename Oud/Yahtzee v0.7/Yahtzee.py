from tkinter import *
import random
import os
from functools import partial

eenen = 'Eenen'
tween = 'Tween'
drien = 'Drien'
vieren = 'Vieren'
vijven = 'Vijven'
zessen = 'Zessen'
drie_dezelfde = 'Drie Dezelfde'
vier_dezelfde = 'Vier Dezelfde'
full_house = 'Full House'
kleine_straat = 'Kleine Straat'
grote_straat = 'Grote Straat'
yahtzee = 'Yahtzee'
kans = 'Kans'

anim_CAP = 15


class Bord(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master

        self.animatiesCount = 15
        self.knoppenCount = 13
        self.steenImages = []
        self.steenworp = []
        for i in range(1, 7):
            file_path = os.path.join(os.path.curdir, 'Stenen', '{}.gif'.format(i))
            self.steenImages.append(PhotoImage(file=file_path))

        self.canvas = Canvas(width=420, height=500, bg='green')
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.knoppenFrame = Frame(self.master)
        self.knoppenFrame.grid(row=1, column=1, sticky='news')

        self.worpButton = Button(self.knoppenFrame, text="Werp Stenen", font=('Impact', 30),
                                 command=partial(self.werpstenen, 50))
        self.worpButton.grid(row=0, column=0, rowspan=7, sticky='news')

        self.categorieen = [eenen, tween, drien, vieren, vijven, zessen, drie_dezelfde, vier_dezelfde, full_house,
                            kleine_straat, grote_straat, yahtzee, kans]

        self.scores = {i: 0 for i in self.categorieen}

        self.spelButtons = {}
        mcol = 1
        mrow = 0
        for t in self.categorieen:
            self.spelButtons[t] = Button(self.knoppenFrame, text=t, command=partial(self.knop_klik, t))
            self.spelButtons[t].grid(row=mrow, column=mcol, sticky='news')
            mcol += 1
            if mcol == 3:
                mcol = 1
                mrow += 1

        self.schermFrame = Frame(self.master)
        self.schermFrame.grid(row=0, column=2, rowspan=3)
        self.scherm = {}

        r = 0
        for i in self.categorieen:
            t = Label(self.schermFrame, text=i, font=('Impact', 20))
            c = Canvas(self.schermFrame, height=60, width=270, bg='green')
            s = Label(self.schermFrame, text='', font=('Impact', 1))
            o = Canvas(self.schermFrame, height=60, width=50, bg='green')
            t.grid(row=r, column=0, sticky='news')
            c.grid(row=r, column=1, sticky='news')
            s.grid(row=r, column=2, sticky='news')
            o.grid(row=r, column=3, sticky='news')
            r += 1
            self.scherm[i] = [t, c, s, o]

    def knop_klik(self, text):
        if not self.steenworp:
            return
        self.knoppenCount -= 1
        self.spelButtons[text].config(state=DISABLED)
        self.scores[text] = self.steenworp
        self.steenworp.sort()
        self.schermstenen(self.scherm[text][1], self.steenworp, 30)
        self.steenworp = []
        if self.knoppenCount == 0:
            self.score_spel()
            return
        else:
            self.canvas.delete("all")
            self.worpButton.config(state=NORMAL)

    def schermstenen(self, canvas, stenen, start):
        if len(stenen) == 0:
            return
        x = 30
        for i in range(5):
            canvas.create_image((x, start), image=self.steenImages[stenen[i] - 1])
            x += 53

    def schermsteenworp(self, canvas, stenen, start):
        if len(stenen) == 0:
            return
        x = 30
        for i in range(5):
            canvas.create_image((x, start + random.randint(-10, 10)), image=self.steenImages[stenen[i] - 1])
            x += 50 + (anim_CAP - self.animatiesCount) * 2

    def werpstenen(self, start):
        if self.animatiesCount == anim_CAP:
            self.worpButton.config(state=DISABLED)
        self.steenworp = [random.randint(1, 6) for x in range(5)]
        if self.animatiesCount == 0:
            self.canvas.delete("all")
            self.schermsteenworp(self.canvas, self.steenworp, start)
            self.animatiesCount = anim_CAP
            return
        else:
            self.canvas.delete("all")
            self.schermsteenworp(self.canvas, self.steenworp, start)
            self.animatiesCount -= 1
            self.master.after(60, self.werpstenen, start + random.randint(10, 30))

    def score_eenen(self):
        totaal1 = 0
        totaal1 += self.scores[eenen].count(1)

    def score_spel(self):
        totaal = 0
        totaalboven = 0
        bonus = 0
        totaalbonus = 0
        totaalonder = 0
        totaal += self.scores[eenen].count(1)
        totaal += self.scores[tween].count(2) * 2
        totaal += self.scores[drien].count(3) * 3
        totaal += self.scores[vieren].count(4) * 4
        totaal += self.scores[vijven].count(5) * 5
        totaal += self.scores[zessen].count(6) * 6
        totaalboven += self.scores[eenen].count(1)
        totaalboven += self.scores[tween].count(2) * 2
        totaalboven += self.scores[drien].count(3) * 3
        totaalboven += self.scores[vieren].count(4) * 4
        totaalboven += self.scores[vijven].count(5) * 5
        totaalboven += self.scores[zessen].count(6) * 6
        totaalbonus += self.scores[eenen].count(1)
        totaalbonus += self.scores[tween].count(2) * 2
        totaalbonus += self.scores[drien].count(3) * 3
        totaalbonus += self.scores[vieren].count(4) * 4
        totaalbonus += self.scores[vijven].count(5) * 5
        totaalbonus += self.scores[zessen].count(6) * 6
        benodigde_score_voor_bonus = 63
        if totaalbonus >= benodigde_score_voor_bonus:
            totaal += 35
            bonus += 35


        for i in set(self.scores[drie_dezelfde]):
            if self.scores[drie_dezelfde].count(i) == 3:
                totaal += sum(self.scores[drie_dezelfde])

        for i in set(self.scores[vier_dezelfde]):
            if self.scores[vier_dezelfde].count(i) == 4:
                totaal += sum(self.scores[vier_dezelfde])

        twee = False
        drie = False
        for i in self.scores[full_house]:
            if self.scores[full_house].count(i) == 3:
                drie = True
            if self.scores[full_house].count(i) == 2:
                twee = True
        if twee and drie:
            totaal += 25
            totaalonder += 25

        st = set(self.scores[kleine_straat])
        if set('1234').issubset(st) or set('2345').issubset(st) or set('3456').issubset(st):
            totaal += 30
            totaalonder += 30

        st = set(self.scores[grote_straat])
        if set('12345').issubset(st) or set('23456').issubset(st):
            totaal += 40
            totaalonder += 40

        if len(set(self.scores[yahtzee])) == 1:
            totaal += 50
            totaalonder += 50

        totaal += sum(self.scores[kans])
        totaalonder += sum(self.scores[kans])

        self.canvas.create_text(200, 50, text="Totaal Boven: {}".format(totaalboven), font=('Impact', 20))
        self.canvas.create_text(200, 100, text="Bonus Score: {}".format(bonus), font=('Impact', 20))
        self.canvas.create_text(200, 150, text="Totaal Onder: {}".format(totaalonder), font=('Impact', 20))
        self.canvas.create_text(200, 200, text="Totale Score: {}".format(totaal), font=('Impact', 40))


root = Tk()
mijnbord = Bord(root)
mijnbord.mainloop()
