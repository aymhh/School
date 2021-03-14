# By: Ameer Al-Shamaa
# This will list all the elements in the "cd.xml" file along with it's properties.

import xml.etree.ElementTree as ET
tree = ET.parse('cd.xml')
root = tree.getroot()

childPicker = 0
subChildPicker = 0
cdCount = 1

print(f"Author of this tree is {root.attrib['author']}")
print(f"There are {len(root)} element(s) in this tree.")
print("These are the current children in the tree:")

for children in root:

    print(f"💿 {children.tag} number {cdCount}")
    cdCount += 1

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # title
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # artist
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # country
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # company
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: ${root[childPicker][subChildPicker].text}") # price
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # year

    subChildPicker = 0
    childPicker += 1

