from random import randint
from .decorators import log
from .userinput import ask_number, ask_number_attempts


class Game:
    def __init__(self, name):
        self.name = name

    def start(self):
        pass
        
    def showName(self):
        print("Welkom bij het spel: " + self.name)

class GuessNumber(Game):
    def __init__(self, use_hints = False, numberofnumbers = 10):
        super().__init__("GuesNumbers")
        self.numbercount = numberofnumbers
        self.hints = use_hints

    def game_over(self, won):
        # NEW: als er geen geheim getal is 
        if won:
            # NEW: print gewonnen!
            print("U heeft het spel gewonnen!")
        # NEW: anders
        else:
            # NEW: print verloren
            print("Helaas, u heeft het spel verloren!")
    def play_round(self, getal):
        '''
        dfjglkfdjgdjk
        '''
        geradengetal = -1
        aantalpogingen = 0
        # zolang geradengetal niet gelijk is aan geheimgetal is en aantalpogingen < 3
        while geradengetal != getal and aantalpogingen < 3:
            # vraag om een getal, geef de gebruiker drie kansen om een goed getal op te geven
            geradengetal = ask_number_attempts(10)
            # geef een hint
            if geradengetal != getal and self.hints:
                print("Het getal is " + ("lager" if getal < geradengetal else "hoger"))
            # hoog aantalpogingen op
            aantalpogingen += 1

        # als geradengetal gelijk is aan geheimgetal
        if  geradengetal == getal:
        #   schrijf goed zo gewonnen!
            print("Goed zo, gewonnen! Het getal was inderdaad " + str(getal))
        # anders
        else:
        #   schrijf helaas, het getal was geheimgetal
            print("Helaas het getal was " + str(getal))

        return geradengetal == getal
    def start(self):
        # maak een lijst met geheimegetallen = [1,2,3]
        geheimegetallen = [randint(0,9) for i in range(self.numbercount)].copy() #//
        # haal het volgende getal van de lijst en onthoud deze in geheimgetal
        geheimgetal = geheimegetallen.pop()
        # schrijf introductietekst
        print(f"Welkom bij raad een getal onder de 10, raad {len(geheimegetallen)+1} getallen")

        # zolang er een geheim getal is en een speelronde succesvol is afgerond....
        while geheimgetal != None and self.play_round(geheimgetal):
            # haal het volgende getal van de lijst en onthoud deze in geheimgetal
            geheimgetal = None if len(geheimegetallen) == 0 else geheimegetallen.pop()
        # druk het resultaat van het spel af...
        self.game_over(geheimgetal == None)







