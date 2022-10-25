
from time import sleep

winkelwagen = []
winkelwagen.clear()
while True:

    print(" Wil je wat toevoegen aan je lijst ? (ja/nee)")
    sleep(1)
    antwoord1 = input("vul hier ja of nee in!")
    if antwoord1 == ("nee"):
        continue
        break

    if antwoord1 == ("ja"):

        print("Top, vul nu in wat u wilt toevoegen aan uw winkelwagen")
        antwoord1a = input()
        winkelwagen.insert(0,antwoord1a)
        print ("Uw winkelwagen bevat nu", winkelwagen)
        print("wilt u iets eruit halen,of iets toevoegen ? (eruit/toevoegen)")
        vraag2 = input()
        
        if vraag2 == ("eruit"):
            print('wat wilt u uit de winkelwagen halen')
            antwoord2 = input()
            winkelwagen.remove(antwoord2)
        if vraag2 == ("toevoegen"):
            print("Top, vul nu in wat u wilt toevoegen aan uw winkelwagen")
            antwoord3 = input()
            winkelwagen.insert(-0,antwoord3)


        

