import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)