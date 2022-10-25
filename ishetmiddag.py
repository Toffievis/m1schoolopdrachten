import time

current_time = time.localtime()
print(current_time)
if current_time.tm_hour >= 12:
    print("het is middag")
elif current_time.tm_hour <18:
    print("het is avond")
elif current_time.tm_hour <24:
    print("het is nacht")
elif current_time.tm_hour <6:
    print("het is ochtend")


def my_function():
    print("je moeder")

my_function()
print("1")
print("2")
my_function()
print("3")