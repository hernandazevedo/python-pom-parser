import argparse
from pathlib import Path


from lib import adjustPom
 
parser = argparse.ArgumentParser(description="Maven pom adjustments for publishing flutter modules on a maven repository ",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--folder", help="Root folder to lookup for pom files", required=True)
parser.add_argument("-g", "--groupId", help="GroupId to replace on pom files")

args = parser.parse_args()
config = vars(args)

for path in Path(config.get("folder")).rglob('*.pom'):
    adjustPom(filename=str(path.absolute()), newGroupId=config.get("groupId"))

