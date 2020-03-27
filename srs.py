import xml.etree.ElementTree as ET

def parseXML(file_name):
    ns = {'body': 'http://schemas.xmlsoap.org/soap/envelope/'}
   # Parse XML with ElementTree
    tree = ET.ElementTree(file=file_name)
    print(tree.getroot())
    root = tree.getroot()
    print('-'*25)
    print('Root')
    print('-'*25)

    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

   # get the information via the children!
    print('-'*25)
    print('Root[0] - Body')
    print('-'*25)
    print("tag=%s, attrib=%s" % (root[0].tag, root[0].attrib))
    print(root[0].tag)
    print(root[0].attrib)

    print('-'*25)
    print('Root[0][0] - Export Profiles Paged Response')
    print('-'*25)
    print("tag=%s, attrib=%s" % (root[0][0].tag, root[0][0].attrib))
    print(root[0][0])

    print('-'*25)
    print('Root[0][0][0] - ReturnCode')
    print('-'*25)
    print("tag=%s, attrib=%s" % (root[0][0][0].tag, root[0][0][0].attrib))
    print('tag=%s, value=%s' % (root[0][0][0].tag, root[0][0][0].text))

    print('-'*25)
    print('Root[0][0][5] - Return Company Data')
    print('-'*25)
    print('tag=%s, value=%s' % (root[0][0][5].tag, root[0][0][5].text))

    print('-'*25)
    print('Root[0][0][5][0] - Return Company Data')
    print('-'*25)
    print('tag=%s, value=%s' % (root[0][0][5][0].tag, root[0][0][5][0].text))

    for child in root[0][0][5][0]:
        print('tag=%s, value=%s' % (child.tag, child.text))

    for mydate in root.iter('lastAnswerDate'):
        print(mydate.text)
 
if __name__ == "__main__":
   parseXML("SRS_example.xml")