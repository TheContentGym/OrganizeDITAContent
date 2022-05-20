import os
from pathlib import Path
SUBDIRECTORIES = {
    "DITA": ['.dita','.xml'],
    "DITAMAPS":['.ditamap'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "ARTWORK": ['.jpg','.jpeg','.png'],
    "LOC_SOURCE":['.SNAG ','.ai']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()
