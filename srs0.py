import xml.etree.ElementTree as ET

def parseXML(file_name):
   # Parse XML with ElementTree
    tree = ET.ElementTree(file=file_name)
    root = tree.getroot()
    print('-'*25)
    print('Root')
    print('-'*25)
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

   # get the information via the children!

    for thing in root.iter():
        print(thing.tag, thing.attrib)

if __name__ == "__main__":
   parseXML("SRS_example.xml")
