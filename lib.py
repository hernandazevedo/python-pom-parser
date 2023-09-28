import xml.etree.ElementTree as ET
import os, fnmatch

NAMESPACE = 'http://maven.apache.org/POM/4.0.0'
PRE = "{" + NAMESPACE +"}"
GROUP_ID = PRE + "groupId"
DEPENDENCIES = PRE + "dependencies"
DEPENDENCY = PRE + "dependency"
VERSION = PRE + "version"
ARTIFACT_ID = PRE + "artifactId"
DEFAULT_MODULE_ID = "flutter_release"

class Pom:
    def __init__(self, pomFile, tree):
        self.pomFile = pomFile
        self.tree = tree
class Config:
    def __init__(self, config):
        self.folder = str(config.get("folder"))
        self.groupId = str(config.get("groupId"))
        self.moduleName = str(config.get("moduleName"))
        self.moduleVersion = str(config.get("moduleVersion"))
        self.pluginVersion = str(config.get("pluginVersion"))
        self.pluginGroupId = str(config.get("pluginGroupId") or config.get("groupId"))

    def toString(self): return """Config(folder: {folder}, groupId: {groupId}, moduleName: {moduleName}, moduleVersion: {moduleVersion}, pluginVersion: {pluginVersion}, pluginGroupId: {pluginGroupId} )
    """.format(folder = self.folder, groupId = self.groupId, moduleName = self.moduleName, moduleVersion = self.moduleVersion, pluginVersion = self.pluginVersion, pluginGroupId = self.pluginGroupId)   

# Parser for python 2.7
# parser = CommentedTreeBuilder()
# 
# class CommentedTreeBuilder(ET.XMLTreeBuilder):
#     def __init__(self, *args, **kwargs):
#         super(CommentedTreeBuilder, self).__init__(*args, **kwargs)
#         self._parser.CommentHandler = self.comment

#     def comment(self, data):
#         self._target.start(ET.Comment, {})
#         self._target.data(data)
#         self._target.end(ET.Comment)

def getElementTree(pomFile):
    # Parser for python 2.7
    # parser = CommentedTreeBuilder()
    # 

    # Parser for python3
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

    ET.register_namespace('', NAMESPACE) 
    tree = ET.parse(pomFile, parser)
    return tree

def adjustPomDependencies(artifactId, pomList, config) : 
    print("adjustPomDependencies artifactId: {artifactId} \n with config: {config} ".format(artifactId = artifactId.text, config = config.toString()))
    
    for pom in pomList:
        root = pom.tree.getroot()
        dependencies = root.find(DEPENDENCIES)
        if(dependencies != None):
            for dependency in dependencies:
                depArtifactId = dependency.find(ARTIFACT_ID)
                depVersion = dependency.find(VERSION)
                depGroupId = dependency.find(GROUP_ID)
                if(depArtifactId.text == artifactId.text):    
                    depVersion.text = config.pluginVersion
                    depGroupId.text = config.pluginGroupId


def adjustPom(pom, pomList, config) : 
    print("adjustPom pomFile: {pomFile} \n with config: {config} ".format(pomFile = pom.pomFile, config = config.toString()))
    root = pom.tree.getroot()
    artifactId = root.find(ARTIFACT_ID)
    version = root.find(VERSION)
    
    groupId = root.find(GROUP_ID)
    groupId.text = config.groupId
    
    if(artifactId.text == DEFAULT_MODULE_ID):    
        version.text = config.moduleVersion
        artifactId = root.find(ARTIFACT_ID)
        artifactId.text = config.moduleName
    else:
        version.text = config.pluginVersion
        adjustPomDependencies(artifactId=artifactId, pomList=pomList, config=config)

def findFiles(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename        