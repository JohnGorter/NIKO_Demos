

def ask_number(attempt):
    try:
        geradengetal = int(input("Geef een getal"))
        return geradengetal
    except:
        if (attempt - 1) != 0:
            print("Geef wel even een getal op, aub poging[ nog " + str(attempt-1) + " pogingen]")
        return None
def ask_number_attempts(attempts):
    # vraag om een getal
    geradengetal = ask_number(attempts)
    tries = 0
    while geradengetal == None and tries < (attempts - 1):
        tries += 1
        geradengetal = ask_number(attempts - tries)   

    if geradengetal == None:
        raise ValueError('3 keer geen goed getal opgegeven')
    return geradengetal