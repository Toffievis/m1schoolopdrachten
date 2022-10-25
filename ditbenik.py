from difflib import Differ


print("hello you, what is your name?: ")
name = input("enter username:")
print("i think that", name + " is a cool name")

print("what year were you born?")
birthyear = int(input("enter year:"))
x = int(2022) 
age = (x - birthyear)
print("oh cool, than that makes you ", (age))

print(name , "do you want to anwser some more questions?")
choice = input()
if choice == 'yes':
    print("oki here we go")
elif choice == 'no': 
    print("alright have a good day, byee")

print("what year whas your mom born?")
momyear = int(input("enter year  ")) 
mompregyear= (x-momyear)
print("alright so ur mom is", mompregyear)
print("so ur mom whas pregnant at age", (mompregyear - age))







while True: 
    print("hoi, ik ben mick. ik ben nieuw op het media college amsterdam, wat is jou naam?: ")
    name = input("hier je naam:")
    print("ik ga je vragen stellen antwoord daarbij alleen met a, b, c, geen hoofdletters")
    print("voordat ik naar het mediacollege amsterdam ging zat ik op")
    print("A. groenhuis wellant mavo aalsmeer")
    print("B. oostbeek wellant mavo aalsmeer")
    print("C. westplas wellant aalsmeer")
    
    choice = input()
    if choice == 'a':
        print("noh man, deze school bestaat niet eens")
    elif choice == 'b': 
        print("nee helaas, dit antwoord is fout")
    elif choice == 'c':
        print("wajoow je hebt het goed hoe wist je dit")
        antwoord1 = input("vul hier in hoe je dit antwoord wist: ")
        print("oh wajoow ik wist het")
    print("oke op naar vraag 2!")
    print("vraag 2. wat was mijn favoriete hobby vroeger?")
    print("A. vissen")
    print("B. skieën")
    print("C. waterpolo")

    choice2 = input()
    if choice2 == "a": 
        print("dit is het goede antwoord, bravo")
        antwoord2 = input("deze had je gegokt zeker ? ja of nee           ")
        if antwoord2 == "ja":
            print("ik wist het, deze keer heb je geluk")
        elif antwoord2 == "nee":
            print("respect naar jou")
    elif choice2 == 'b': 
        print("hahaha had je dit van mij verwacht ja, maar nee het is fout")
    elif choice2 == 'c':
        print("haha wie speeld er nou weer waterpolo, ik niet in ieder geval")
   

    print("oke we zijn aangekomen bij de laatste vraag!")
    print("vraag 3. wat is mijn bijbaan op dit moment")


    print("A. pizza koerier bij new york pizza")
    print("B. shiftrunner bij dominos pizza")
    print("C. vakkenvuller bij de jumbo")

    choice3 = input()
    if choice3 == "a": 
        print("het zou je baan maar wel zijn kut new york pizza")

    elif choice3 == 'b': 
        print("jaman ik werk hier al 4 jaar, gefeliciteerd met dit goede antwoord")
    elif choice3 == 'c':
        print("mij niet gezien hoor")

    print("dit was het, wil je dit opnieuw doen?")
    if input("wil je nog een keer? (J/N)").strip().upper() != 'J':
        break