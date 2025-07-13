from xml.dom import minidom
#Parsing the xml file
tree = minidom.parse("myxml.xml")
#print(tree)

#Get the tagname
#tagname = tree.getElementsByTagName('name')[1]
#print(tagname.firstChild.data)

#To display all the tags
#tagname = tree.getElementsByTagName('address')
#for i in tagname:
#    print(i.firstChild.data)

#Length of data
tagname = tree.getElementsByTagName('address')
print(len(tagname))