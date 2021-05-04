# By: Ameer Al-Shamaa
# Date: 29/03/2021
# binarySearch.py
# An alogrithim loop (linear) to sort through the pokemon collection and iniaite swaps if no pokemon exists within current array


from pokemonArray import pokemonList # Import's the pokemon character list from another moudle.

def linearSearch(array, item): #Initiates the linearSearch function and takes in 2 elements, 
    found = False # Sets the flag
    for index in range(len(array)): # Loops depending on how many elements are within the list
        if array[index] == item: # If the element has been found then set the flag to found
            found = True # Updates the flag
    return found # returns the outcome

pokemonToBeTraded = input("What is the code of the pokemon you are looking to swap with?\n") #Ask's the users for the ID of the pokemon that will be used in the searching alogrithim


if(pokemonToBeTraded.startswith("#")): # Slices off the # if inputed
    pokemonToBeTraded = pokemonToBeTraded[1:]

if(pokemonToBeTraded.islower() or pokemonToBeTraded.isupper()): # Range checker to only accept numbers
    print("Can't have that!\nOnly put in the number code of the pokemon itself! 🔢")
    exit()

collectionResult = linearSearch(pokemonList, pokemonToBeTraded) # Calls in the searchingAlogrithim function, pokemon list and user input

if (collectionResult == True): # If the pokemon is in the list, respond with:
    print(f"Hold on a second there adventurer! ⛔\n- You already own the {pokemonToBeTraded} pokemon, do not do the swap!")
elif (collectionResult == False): #If the pokemon is NOT in the list, repond with:
    print("Woohoo!\n- You don't own this pokemon, go catch em'! 🐢")