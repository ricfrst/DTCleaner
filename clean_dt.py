import os
import shutil
import logging
from pathlib import Path

#log setup
logs = Path.home() / "Documents" / "DTCleaner.log" #saved location
logging.basicConfig(
    filename= logs, # where to store
    level=logging.INFO,# INFO WARNING ERROR CRITICAL NODEBUG
    format="%(levelname)s - %(message)s"
)


#defining extensions
img_extensions = {".jpg",".png",".jpeg"}
doc_extensions = {".docx",".doc",".txt",".xlsx","pptx"}
shortcut_extension = ".lnk"



#define destinations
#unchanged as of4/9
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
    logging.info(f"Moved: {file_path} → {destination}")


#function to delete
def dump (file_path):
    file_path.unlink()
    logging.info(f"dumped {file_path}")


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
        print(f"DUMPED ::  {file_path.name}")
    else:
        dump(file_path)
        print(f"DUMPED ::  {file_path.name}")



def cleanitup():
    for item in dt_path.iterdir():
        if item.is_file():
            sorter(item)
        elif item.is_dir():
            destination = documents / item.name
            shutil.move(str(item),str(destination))
            # Check if the folder is empty after moving
            if not any(destination.iterdir()):  # If folder is empty, delete it
                destination.rmdir()
                logging.info(f"DUMPED EMPTY FOLDER: {destination}")
                print(f"Deleted empty folder :: {destination}")


cleanitup()
print(f"Cleaning complete! Logs saved at: {logs}")
