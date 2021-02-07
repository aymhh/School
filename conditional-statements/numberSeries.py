import time

x = input("What number do you want to start the count from?\n")
while not x.isnumeric():
    x = input("That is not a number...\nWhat number do you want to start the count from?\n")
xInt = int(x)

y = input("What number do you want to end the count on?\n")
while not y.isnumeric():
    y = input("What number do you want to end the count on?\n")
yInt = int(y) + 1

numberRange = list(range(xInt, yInt))

print("calculating...")
time.sleep(1)

evenNumbers = []
oddNumbers = []

for calculatedNumbers in numberRange:
    if(calculatedNumbers%2 == 0):
        evenNumbers.append(calculatedNumbers)
    else:
        oddNumbers.append(calculatedNumbers)

print(evenNumbers)
print(f"Number of even numbers: {str(len(evenNumbers))}")
print(oddNumbers)
print(f"Number of odd numbers: {str(len(oddNumbers))}")