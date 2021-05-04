# By: Ameer Al-Shamaa
# Date: 29/03/2021
# binarySearch.py
# An alogrithim loop (binary) to sort through the pokemon collection and iniaite swaps if no pokemon exists within current array

from pokemonArray import pokemonList # Import's the pokemon character list from another moudle.

def binarySearchAlgo(array,item): #Initates the creation of the binarySearch alogrithim and taking in 2 inputs 
    firstElement = 0 
    lastElement = len(array) - 1 # Finds the last element from an array index search
    found = False # Sets the flag checker

    while(firstElement <= lastElement and not found): # Looping till the first element in the list is less than or equal to the last element in the list and remains till not found
        middleIndex = (firstElement + lastElement)//2 # Collects the middle index of the list
        
        if array[middleIndex] == item: #If the middle element in the array is the item to searched for then the flag updates and the element has been found
            found = True
        
        else: # Else if the middle element has not been found in the recent callback then
            
            if item < array[middleIndex]: 
                lastElement = middleIndex - 1
            
            else:
                firstElement = middleIndex + 1	
    return found

pokemonToBeTraded = input("What is the code of the pokemon you are looking to swap with?\n") #Ask's the users for the ID of the pokemon that will be used in the searching alogrithim


if(pokemonToBeTraded.startswith("#")): # Slices off the # if inputed
    pokemonToBeTraded = pokemonToBeTraded[1:]

if(pokemonToBeTraded.islower() or pokemonToBeTraded.isupper()): # Range checker to only accept numbers
    print("Can't have that!\nOnly put in the number code of the pokemon itself! 🔢")
    exit()

collectionResult = binarySearchAlgo(pokemonList, pokemonToBeTraded) # Calls in the searchingAlogrithim function, pokemon list and user input

if (collectionResult == True): # If the pokemon is in the list, respond with:
    print(f"Hold on a second there adventurer! ⛔\n- You already own the {pokemonToBeTraded} pokemon, do not do the swap!")
elif (collectionResult == False): #If the pokemon is NOT in the list, repond with:
    print("Woohoo!\n- You don't own this current pokemon, go catch em'! 🐢")