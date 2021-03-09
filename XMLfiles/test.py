from xml.dom import minidom

file = minidom.parse('items.xml')

elements = file.getElementsByTagName("child")

print(elements[0].attributes['location'].value)