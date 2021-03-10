import time

number1 = int(input("This is a simple addition calculator, input the first number please!\n"))
number2 = int(input("What is the second number?\n"))
result = number1 + number2

print("Calculating...")
time.sleep(1)
print(f"The answer is:\n{number1 + number2}")