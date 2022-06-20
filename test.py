import os
from xml.etree import ElementTree
from lxml import etree
import xml.etree.ElementTree as ET


fileName = 'sampleData.xml'
fullFile = os.path.abspath(os.path.join('data',fileName))
#print(fullFile)

dom = ElementTree.parse(fullFile)
#print(dom)

race = dom.findall('CD/TITLE')
print(race)


for r in race:

    print(r.text)

if __name__ == '__main__':
    print()
