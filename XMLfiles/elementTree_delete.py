# By: Ameer Al-Shamaa
# This will select a child from the tree and delete's it

import xml.etree.ElementTree as ET
tree = ET.parse('cd.xml')
root = tree.getroot()

