from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ElementTree

NAMESPACE = 'http://maven.apache.org/POM/4.0.0'
PRE = "{" + NAMESPACE +"}"
GROUP_ID = PRE + "groupId"
DEPENDENCIES = PRE + "dependencies"
DEPENDENCY = PRE + "dependency"
VERSION = PRE + "version"
ARTIFACT_ID = PRE + "artifactId"
DEFAULT_MODULE_ID = "flutter_release"
class Config:
    def __init__(self, config: dict[str, Any]):
        self.folder: str = config.get("folder")
        self.groupId: str = config.get("groupId")
        self.moduleName: str = config.get("moduleName")
        self.moduleVersion: str = config.get("moduleVersion")
        self.pluginVersion: str = config.get("pluginVersion")

    def toString(self): return """Config(folder: {folder}, groupId: {groupId}, moduleName: {moduleName}, moduleVersion: {moduleVersion}, pluginVersion: {pluginVersion} )
    """.format(folder = self.folder, groupId = self.groupId, moduleName = self.moduleName, moduleVersion = self.moduleVersion, pluginVersion = self.pluginVersion)   

def getElementTree(pomFile: str) -> ElementTree:
    parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))
    ElementTree.register_namespace('', NAMESPACE) 
    tree = ElementTree.parse(pomFile, parser)
    return tree

def adjustPom(pomFile: str, pomList: list[Path], config: Config) : 
    print("Parsing pomFile: {pomFile} \n with config: {config} ".format(pomFile = pomFile, config = config.toString()))
    tree: ElementTree = getElementTree(pomFile=pomFile)
    root = tree.getroot()
    artifactId = groupId = root.find(ARTIFACT_ID)
    version = root.find(VERSION)
    if(artifactId.text == DEFAULT_MODULE_ID):    
        version.text = config.moduleVersion
        artifactId = root.find(ARTIFACT_ID)
        artifactId.text = config.moduleName
    else:
        version.text = config.pluginVersion

    groupId = root.find(GROUP_ID)
    groupId.text = config.groupId
    
    tree.write(pomFile +".tmp")