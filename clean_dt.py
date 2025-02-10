import os
from pathlib import Path


#get desktop path
dt_path = Path.home()/"Desktop"

#string to print
#f to replace path var with actual path name, just easier to read
print(f"The path in question : {dt_path}")

#list dt items
for item in dt_path.iterdir():
    if item.is_dir():
        print(f"FOLDER {item}")
    elif item.is_file():
        file_extension = item.suffix.lower()  # Get the file extension and make it lowercase
        print(f"FILE {item}| Extension:{file_extension}")