numbers = []

for x in range(1500, 2700):
    if (x%7 == 0) and (x%5 == 0):
        numbers.append(str(x))
print(f"these are all the numbers that are fully divisable by 5 and 7:\n{numbers}")
