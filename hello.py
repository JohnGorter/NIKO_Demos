# Spel raad het getal
from random import randint

def game_over(won):
    # NEW: als er geen geheim getal is 
    if won:
        # NEW: print gewonnen!
        print("U heeft het spel gewonnen!")
    # NEW: anders
    else:
        # NEW: print verloren
        print("Helaas, u heeft het spel verloren!")
def play_round(getal):
    geradengetal = -1
    aantalpogingen = 0
     # zolang geradengetal niet gelijk is aan geheimgetal is en aantalpogingen < 3
    while geradengetal != getal and aantalpogingen < 3:
    #   vraag om een getal
        geradengetal = int(input("Geef een getal"))
    #   hoog aantalpogingen op
        aantalpogingen += 1
    # als geradengetal gelijk is aan geheimgetal
    if  geradengetal == geheimgetal:
    #   schrijf goed zo gewonnen!
        print("Goed zo, gewonnen!")
    # anders
    else:
    #   schrijf helaas, het getal was geheimgetal
        print("Helaas het getal was " + str(geheimgetal))

    return geradengetal == geheimgetal

# maak een lijst met geheimegetallen = [1,2,3]
geheimegetallen = [randint(0,9) for i in range(10)].copy() #//
# haal het volgende getal van de lijst en onthoud deze in geheimgetal
geheimgetal = None # geheimegetallen.pop()
# schrijf introductietekst
print(f"Welkom bij raad een getal onder de 10, raad {len(geheimegetallen)+1} getallen")

# zolang er een geheim getal is en een speelronde succesvol is afgerond....
while geheimgetal != None and play_round(geheimgetal):
    # haal het volgende getal van de lijst en onthoud deze in geheimgetal
    geheimgetal = None if len(geheimegetallen) == 0 else geheimegetallen.pop()
    
# druk het resultaat van het spel af...
game_over(geheimgetal == None)