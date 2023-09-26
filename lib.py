import xml.etree.ElementTree as ElementTree

NAMESPACE = 'http://maven.apache.org/POM/4.0.0'
PRE = "{" + NAMESPACE +"}"
GROUP_ID = PRE + "groupId"
DEPENDENCIES = PRE + "dependencies"
DEPENDENCY = PRE + "dependency"
VERSION = PRE + "version"
ARTIFACT_ID = PRE + "artifactId"

def getElementTree(filename: str) -> ElementTree:
    parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))
    ElementTree.register_namespace('', NAMESPACE) 
    tree = ElementTree.parse(filename, parser)
    return tree

def adjustPom(filename: str, newGroupId: str) : 
    print("Add newGroupId {newGroupId} filename: {filename}".format(filename = filename, newGroupId = newGroupId))
    tree: ElementTree = getElementTree(filename=filename)
    root = tree.getroot()
    grpId = root.find(GROUP_ID)
    grpId.text = newGroupId
    tree.write(filename +".tmp")