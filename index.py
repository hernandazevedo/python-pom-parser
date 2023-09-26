import argparse
from pathlib import Path
from typing import Any
from lib import adjustPom
 
argumentParser = argparse.ArgumentParser(description="Maven pom adjustments for publishing flutter modules on a maven repository ",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argumentParser.add_argument("-f", "--folder", help="Root folder to lookup for pom files", required=True)
argumentParser.add_argument("-g", "--groupId", help="GroupId to replace on pom files", required=True)
argumentParser.add_argument("-m", "--moduleName", help="ArtifactId of the main module to replace the artifact name", required=True)
argumentParser.add_argument("-v", "--version", help="Version for the plugins", required=True)

args = argumentParser.parse_args()
config = vars(args)

def main(config: dict[str, Any]):
    for path in Path(config.get("folder")).rglob('*.pom'):
        adjustPom(filename=str(path.absolute()), newGroupId=config.get("groupId"))

main(config)
