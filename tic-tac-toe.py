print("Willkommen zu Tic-Tac-Toe")

spieler = "X"

brett = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]
def zeige_brett():
    print(f" {brett[0]} | {brett[1]} | {brett[2]}")
    print("---+---+---")
    print(f" {brett[3]} | {brett[4]} | {brett[5]}")
    print("---+---+---")
    print(f" {brett[6]} | {brett[7]} | {brett[8]}")

def pruefe_gewinner():
        gewinn_kombination = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for i in gewinn_kombination:
            if brett[i[0]] == brett[i[1]] == brett[i[2]] != " ":
                print(f"{brett[i[0]]} hat gewonnen")
                return True

        return False    

def pruefe_unentschieden():
    if " " not in brett:
        print("Es ist ein unentschieden")
        return True
    
    return False

spiel_laeuft = True
while spiel_laeuft:

    zeige_brett()

    zug = int(input(f"Spieler {spieler}, wähle ein Feld (1-9): "))
    
    position = zug - 1
    if brett[position] == " ":
        brett[position] = spieler
        
        zeige_brett()

        if pruefe_gewinner():
            spiel_laeuft = False

        elif pruefe_unentschieden():
            spiel_laeuft = False

        else:   
            if spieler == "X":
                spieler = "O"
            else:
                spieler = "X"
    
    else:
        print("Feld ist besetzt")

   

        
        

                                                                                                                    #spieler = x
                                                                                                                    #zug = Stelle, aber unverändert (vermutlich nicht gebraucht)
                                                                                                                    #position = Stelle
                                                                                                                    #brett = spielfeld
    
    
    
    
    
    
    
    
                                                                                        #     Spieler gibt eine Zahl ein
                                                                                        #         ↓
                                                                                        # Zahl wird um 1 kleiner gemacht
                                                                                                #         ↓
                                                                                         # Diese Position wird im Brett benutzt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if x_gewinnt:
    #     spiel_laeuft = False
    # if o_gewinnt:
    #     spiel_laeuft = False
    # if unentschieden:
    #     spiel_laeuft = False


 