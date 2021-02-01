import time

animals = ["turkey", "cow", "horse", "pig", "dog", "cat"]

for animal in animals: 
    print("A " + animal + " is the best")
    if animal == "turkey":
        print("gobble gobble")
        time.sleep(1)

    elif animal == "cow":
        print("Moo Moo")
        time.sleep(1)

    elif animal == "horse":
        print("Neigh")
        time.sleep(1)

    elif animal == "pig":
        print("Oink Oink")
        time.sleep(1)

    elif animal == "dog":
        print("Woof Woof")
        time.sleep(1)

    elif animal == "cat":
        print("Nom Nom")
        time.sleep(1)

print("Just finsihed printing out all the animals and the sounds they produce.")