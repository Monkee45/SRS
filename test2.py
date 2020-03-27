import xml.etree.ElementTree as ET
print('Imported ElementTree')
root = ET.parse('test2.xml').getroot()

print('-'*25)
print('Root.tag')
print('-'*25)
print("TAG = %s, Attributes= %s" % (root.tag, root.attrib))

print('-'*25)
print('Children')
print('-'*25)
for child in root:
    print(child.tag, child.attrib)

print('-'*25)
print('Every Element tag in the file')
print('-'*25)
for thing in root.iter():
    print(thing.tag, thing.attrib)

print('-'*25)
print('Every movie Element in the file')
print('-'*25)
for thing in root.iter('movie'):
    print(thing.tag, thing.attrib)

print('-'*25)
print('All the movie descriptions in the file')
print('-'*25)
for description in root.iter('description'):
    print(description.tag, description.text)

print('-'*25)
print('Searching for Movies from 1992')
print('-'*25)
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

print('-'*25)
print('Find attributes which have multiple set to yes')
print('-'*25)
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']"):
    print(movie.tag, movie.attrib, movie.text)

print('-'*25)
print('FInd movies available in multiple formats')
print('-'*25)
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.tag, movie[1].text)

print('-'*25)
print('FInd movies available in multiple formats')
print('-'*25)
for movie in root.findall("./genre/decade/movie/[@title]"):
    print(movie.tag, movie.attrib["title"])
