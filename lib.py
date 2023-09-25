import xml.etree.ElementTree as ElementTree

namespace = 'http://maven.apache.org/POM/4.0.0'
pre = "{" + namespace +"}"

def adjustPom(filename: str, newGroupId: str) : 
    print("Add newGroupId {newGroupId} filename: {filename}".format(filename = filename, newGroupId = newGroupId))
    parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))
    ElementTree.register_namespace('', namespace) 
    tree = ElementTree.parse(filename, parser)
    root = tree.getroot()
    grpId = root.find(pre + "groupId")
    grpId.text = newGroupId
    tree.write(filename +".tmp")