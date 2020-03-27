import xml.etree.ElementTree as ET
print('Imported ElementTree')
root = ET.parse('test.xml').getroot()

print('Root', root)
print('-'*25)
print('Root[0]')
print('-'*25)
print(root[0])

print('-'*25)
print('Root[0][0]')
print('-'*25)
print(root[0][0])
print("tag=%s, attrib=%s" % (root[0][0].tag, root[0][0].attrib))

print('-'*25)
print('Root[0][0][0]')
print('-'*25)
print(root[0][0][0].attrib)
print("tag=%s, attrib=%s" % (root[0][0][0].tag, root[0][0][0].attrib))
print(root[0][0][0].text)



print('Entering the For Loop')
for child in root.iter('neighbour'):
    print(child.tag, child.attrib)
    
print('FindAll')

for listing in root.findall('listing'):
    print(listing)
    for country in listing:
        print(country.attrib)



for item in root.findall('./listing/country'):
    print(item.attrib)
#    rank = country.find('rank').text
#    name = country.get('name')
#    print(name, rank)



