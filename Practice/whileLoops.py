import time

play = True

while play:

    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    print("Calculating...")

    time.sleep(1)

    print("Addition:", x + y)
    time.sleep(0.5)
    print("Subtraction", x - y)
    time.sleep(0.5)
    print("Multiplication", x * y)
    time.sleep(0.5)
    print("Division", x / y)
    time.sleep(0.5)
    print("Percentage", x % y)

    if input("Play again? ") == "no":
        play = False