# By: Ameer Al-Shamaa
# On: 22/02/2021
# Name: plantStore.py
# A program that iterates over a set of elements within an XML tree

import xml.etree.ElementTree as ET # Import's the element tree moudle and pipes it to the variable of "ET"
tree = ET.parse('plant_store(task2).xml') # Parses the given element tree for python to handle properly
root = tree.getroot() # Gets the root of the reet
childPicker = 0 
subChildPicker = 0
plantCount = 1

for children in root: # Begins iterating the XML file over a set of loops till there is no more chilren to be found withing the tree.
    print(f"{children.tag} {plantCount}") # The plant head (The child element)

    print(f"    {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Common Name of the plant 
    subChildPicker += 1 
    print(f"    {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Botanical Name: of the plant 
    subChildPicker += 1
    print(f"    {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}\n     - Description: {root[childPicker][subChildPicker].attrib['description']}") # Zone of the plant alongside the description 
    subChildPicker += 1
    print(f"    {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Light needed for the plant 
    subChildPicker += 1
    print(f"    {root[childPicker][subChildPicker].tag}: ${root[childPicker][subChildPicker].text}") # Price of the plant

    plantCount += 1 # Increase the plant number to ready for the next given element
    childPicker += 1 # Increase the childPicker to value to move to the next child element within the tree
    subChildPicker = 0 # Resets the subchild value so it can start again at the beginning of the sub children elements
