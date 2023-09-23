import xml.etree.ElementTree as ElementTree
import logging
namespace = 'http://maven.apache.org/POM/4.0.0'
filename = 'beagle-android.pom'

parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))

ElementTree.register_namespace('', namespace) 
tree = ElementTree.parse(filename, parser)
pre = "{" + namespace +"}"
root = tree.getroot()

grpId = root.find(pre + "groupId")



grpId.text = "com.localiza.localizamais"
logging.info("Item: %s", grpId)

 
tree.write('beagle-android.pom.tmp')