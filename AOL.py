import random
a = int(input("What number do you want?"))
if a%2 == 0:
    def multiple(a):
        a = a * (2)
        return a
    print(multiple(a))
if a%2 != 0:
    def subtraction(a):
        a = a - 1
        return a
    print(subtraction(a))


percent = int(input("what is your mark"))


def grade(percent):
    while percent < 0 or percent > 100:
        percent = int(input("That is not a possible grade. Input another one"))
    if percent in range(0,50):
        print("F")
    elif percent in range(50,56):
        print("D-")
    elif percent in range(56,60):
        print("D")
    elif percent in range(61,66):
        print("D+")
    elif percent in range(66,71):
        print("C-")
    elif percent in range(71, 75):
        print("C")
    elif percent in range(75, 80):
        print("C+")
    elif percent in range(80, 84):
        print("B-")
    elif percent in range(84, 88):
        print("B")
    elif percent in range(88, 90):
        print("B+")
    elif percent in range(90, 94):
        print("A-")
    elif percent in range(94, 97):
        print("A")
    elif percent in range(97, 100):
        print("A+")


grade(percent)


num1 = int(input("Give me a number"))
num2 = int(input("Give me another number"))
num3 = int(input("Give me another number"))
def calculation(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    elif num1 == num2 == num3:
        print(num1)


calculation(num1, num2, num3)


rolls = int(input("How many times would you like to roll the dice"))
dice = int(input("how many sides does your dice have"))
def sumdice(dice,rolls):
    sumdice4 = 0
    for x in range(rolls):
        sumdice4 = sumdice4 + random.randint(1, dice)
    return sumdice4

print(sumdice(dice,rolls))
