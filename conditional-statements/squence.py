# 0 1 1 2 3 5 8 13 21

number1 = 0
number2 = 1
upto = 50

print("Fibonacci sequence:")

while number1 >= upto:
    print(number1)
    print(number2)

    weirdNumber = number1 + number2
    number1 = number2
    number2