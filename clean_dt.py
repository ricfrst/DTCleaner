import os
import shutil
from pathlib import Path



#defining extensions
img_extensions = {".jpg",".png",".jpeg"}
doc_extensions = {".docx",".doc",".txt",".xlsx","pptx"}
shortcut_extension = ".lnk"



#define destinations
pictures = Path.home() / "Pictures"
documents = Path.home() / "Documents"
#get desktop path
dt_path = Path.home()/"Desktop"



#string to print
#f to replace path var with actual path name, just easier to read
print(f"The path in question : {dt_path}")



#function to move file
def move (file_path, dst_path):
    destination = dst_path / file_path.name
    shutil.move(file_path, destination)
    print(f"sent to {destination}, {file_path.name}")


#function to delete
def dump (file_path):
    file_path.unlink()
    print(f"sent to shadow realm, {file_path.name}")


#file sorting
def sorter (file_path):
    cur_extension = file_path.suffix.lower()
    if cur_extension in img_extensions:
        print(f"Moved to Pictures folder ::  {file_path.name}")
        move(file_path, pictures)
    elif cur_extension in doc_extensions:
        print(f"Moved to Documents folder ::  {file_path.name}")
        move(file_path, documents)
    elif cur_extension == shortcut_extension:
        dump(file_path)
    else:
        dump(file_path)


def cleanitup():
    for item in dt_path.iterdir():
        if item.is_file():
            sorter(item)
        elif item.is_dir():
            destination = documents / item.name
            shutil.move(str(item),str(destination))


cleanitup()
