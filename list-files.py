from pathlib import Path

for path in Path('repo').rglob('*.pom'):
    print(path.name)