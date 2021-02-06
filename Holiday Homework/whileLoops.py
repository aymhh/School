import time

temperature = 115

while temperature >= 80:
    print(temperature)
    temperature -= 1
    time.sleep(0.1)

print("Temperature is now cool.\nEnjoy!")