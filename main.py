import argparse
from pathlib import Path
from lib import Pom, adjustPom,Config, getElementTree
import xml.etree.ElementTree as ET

 
argumentParser = argparse.ArgumentParser(description="Maven pom adjustments for publishing flutter modules on a maven repository ",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argumentParser.add_argument("-f", "--folder", help="Root folder to lookup for pom files", required=True)
argumentParser.add_argument("-g", "--groupId", help="GroupId to replace on pom files", required=True)
argumentParser.add_argument("-mn", "--moduleName", help="ArtifactId of the main module to replace the artifact name", required=True)
argumentParser.add_argument("-mv", "--moduleVersion", help="Version for the module", required=True)
argumentParser.add_argument("-pv", "--pluginVersion", help="Version for the plugins", required=True)
argumentParser.add_argument("-pg", "--pluginGroupId", help="GroupId for the plugins, if not present, defaults to groupdId")

args = argumentParser.parse_args()
dictionary = vars(args)

#Example: python index.py --folder repo --groupId "com.sample3" --moduleName "mymodulename" --moduleVersion "0.0.1-rc1" --pluginVersion "0.0.1"
def main(config: Config):
    pomList: list[Pom] = list()
    for path in Path(config.folder).rglob('*.pom'):
        pomFile = str(path.absolute())
        pomList.append(Pom(tree=getElementTree(pomFile=pomFile), pomFile=pomFile))

    for pom in pomList:    
        adjustPom(pom=pom, pomList=pomList, config=config)

    #Writing trees on respective files
    for pom in pomList:    
            pom.tree.write(pom.pomFile +".tmp")

main(Config(dictionary))
