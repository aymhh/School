import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()
childPicker = 0
subChildPicker = 0
country = 1

print(f"Author of this tree is {root.attrib['author']}")
print(f"There are {len(root)} element(s) in this tree.")
print("These are the current countries in the tree:")

for children in root:

    print(f"{country} {children.attrib['name']}")
    country += 1

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}")
    subChildPicker += 1

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}")
    subChildPicker += 1

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}, ")
    subChildPicker += 1

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].attrib['name']}")


# keeps looping till all the elements ended WITHOUTH individual input