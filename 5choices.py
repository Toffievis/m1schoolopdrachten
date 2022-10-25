print("belangerijke informatie:")
print("kies bij de optie die je gaat krijgen een van de gegeven antwoorden ")
print("type je antwoord precies zoals het staat in de keuzes")
print("let daarbij op de spelling")
print("ook is belangerijk dat je geen hoofdletters gebruikt")
print("veel plezier!, en alvast bedankt voor het spelen")


while True:
    print("je huis staat in de fik wat doe je ?")
    print("je kan kiezen: rennen, blussen, douchen,112 bellen, blijven zitten")
    choice = input()
    if choice == 'rennen':
        print("ik zou snel gaan rennen man voordat je gebraden word als een chickenwing!")
        break
    elif choice == 'kalli':
        print("dit is een gewaagde keuze, weet je zeker dat je door wilt gaan ?")
        if input("wilt u doorgaan? (ja/nee)").strip().upper() != 'ja':
            exit()
    elif choice == 'blussen':
        print("leeg je aquarium gwn op die vuur")
        break
    elif choice == "douchen": 
        print("dit is een gewaagde keuze, weet je zeker dat je door wilt gaan ?")
        if input("wilt u doorgaan? (ja/nee)").strip().upper() != 'ja':
            print('het boeide je niet dat je huis in de fik stond, je bent gaant douchen')
            print("helaas heeft het je niet gered en je bent game over nu") 
            exit()

    elif choice == ("112 bellen"):
        print("dit is misschien wel de beste keuze")
        break
    elif choice == ("blijven zitten"):
        print("geen angst we got the fire resistance potion dw")
        break
    
    else:
        continue

while True:
    print(" je bent nu onderweg naar buiten maar je kan maar 1 ding meenemen naar buiten! wat kies je ?")
    print("je kan kiezen uit: magnetron, tandenborstel, ei , telefoon of tosti")

    choice = input()
    if choice == 'magnetron':
        print("dit is een basic keuze, had beter van je verwacht")
        break
    elif choice == 'tandenborstel':
        print("dit is een steady keuze, ik denk dat het meerderheid hier voor zal gaan")
        break
    elif choice == 'ei':
        print("dit is een domme keuze wie kiest er nou een ei")
        break
    elif choice == "douchen": 
     print("dit is een gewaagde keuze, weet je zeker dat je door wilt gaan ?")
    if input("wilt u doorgaan? (ja/Nee)").strip().upper() != 'ja':
             break
    elif choice == ("telefoon"):
        print("dit is misschien wel de beste keuze")
    elif choice == ("tosti"):
            print('dit is een zeer smakelijke tosti!')
            if input("curry ? (ja/Nee)").strip().upper() != 'ja':
                break
    else:
        continue


while True:
        print("je bent nu buiten wat doe je?:")
        print("je kan kiezen uit:tosti eten, pappagaai roepen, snap maken") 
        print("babbel met de buurvrouw, sjekkie draaien, terug naar binnen rennen")
        choice = input()
        if choice == 'tosti eten':
            print("je neemt een hap van de perfect warme tosti die krokant laagje heeft opgelopen door die vuur")
            print("maar helaas de kaas is nog te warm en je verbrand een stuk van je toch")
            break
        elif choice == 'pappagaai roepen':
            print("je gekleurde vogel komt naar je toe gevlogen vanuit de boom, hij land op je schouder en je heeft hem een pinda ")
            break
        elif choice == 'snap maken':
            print("je rent  weer je huis in om snel je telefoon nog te pakken") 
            print("je start snap op maar dan valt ineens je telefoon uit")
            print("je hebt nu alle sensatie niet kunnen filmen")
            break
        elif choice == "babbel met de buurvrouw": 
            print("dit is een gewaagde keuze, weet je zeker dat je door wilt gaan ?")
        if input("wilt u doorgaan? (ja/nee)"):
            if choice == "nee" :
                break
            print("je probeert een gesprek met de zuurkijkende buurvrouw te starten alleen is de buurvouw niet geinteresseert")
            print("de buurvrouw heeft je afgemaakt,game over ")
            print("dankjewel voor het spelen!")
            break
        elif choice == ("sjekkie draaien"):
            print("Niks voor mij maar als jij er van houdt ben ik daar oke mee")
            break
        elif choice == ("terug naar binnen rennen"):
            print('je hebt je net bedacht dat je favoriete badslippers nog binnen liggen')
            if input("ga je ze ophalen ? (ja/nee)").strip().upper() != 'ja':
                print("u died for a good cause, rest in pieces brothah")
                break
        else:
            continue
        print("dit is het eind?")
        if input("wil je het opnieuw spelen? (ja/nee)").strip().upper() != 'ja':
            print("dankjewel voor het spelen")
        break
        
