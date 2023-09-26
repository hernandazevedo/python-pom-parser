import argparse
from pathlib import Path
from lib import adjustPom,Config
 
argumentParser = argparse.ArgumentParser(description="Maven pom adjustments for publishing flutter modules on a maven repository ",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argumentParser.add_argument("-f", "--folder", help="Root folder to lookup for pom files", required=True)
argumentParser.add_argument("-g", "--groupId", help="GroupId to replace on pom files", required=True)
argumentParser.add_argument("-m", "--moduleName", help="ArtifactId of the main module to replace the artifact name", required=True)
argumentParser.add_argument("-v", "--moduleVersion", help="Version for the module", required=True)
argumentParser.add_argument("-p", "--pluginVersion", help="Version for the plugins", required=True)

args = argumentParser.parse_args()
dictionary = vars(args)

#Example: python index.py --folder repo --groupId "com.sample3" --moduleName "mymodulename" --moduleVersion "0.0.1-rc1" --pluginVersion "0.0.1"
def main(config: Config):
    pomList: list[Path] = list(Path(config.folder).rglob('*.pom'))
    for path in pomList:
        adjustPom(pomFile=str(path.absolute()), pomList=pomList, config=config)

main(Config(dictionary))
