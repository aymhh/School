# ameer al-shamaa
import random
x = str(random.randint(1, 9))

print(str(x))

guess = input("What's your guess?\nNumbers between 1 - 9 inclusive.\n")

while guess != x:
    print("Incorrect, do it again")
    guess = input("What's your guess?\nNumbers between 1 - 9 inclusive.\n")


print("Woohoo")