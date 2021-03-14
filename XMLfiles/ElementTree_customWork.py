import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

childPicker = 0
subChildPicker = 0

print(f"Author of this tree is {root.attrib['author']}")
print(f"There are {len(root)} element(s) in this tree.")
print("These are the current countries in the tree:")

for children in root:
    print(f"{children.tag}: {children.attrib['name']}") # Country

    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Country rank
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Country Year
    subChildPicker += 1
    print(f"- {root[childPicker][subChildPicker].tag}: {root[childPicker][subChildPicker].text}") # Country GDPPC

    childPicker += 1
    subChildPicker = 0
