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


