def add(a, b):
    print(a+b)

add(6, 9)
def multiply(a, b):
    print(a*b)
multiply(6, 7)

def minus(a, b):
    print(a-b)

def devide(a, b):
    print(a / b)


def check_if_string_is_long(str, length):
    if len(str) > length:
        print("deze strong is tantoe lang")
    else:
        print("deze string is hooptie kort swa")
check_if_string_is_long("hello", 8)
check_if_string_is_long("hello world", 8)

while True:
    sentence = input()
    print(len(sentence)) 
    continue

