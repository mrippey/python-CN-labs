# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from os import path
import pathlib
import shutil
# Find the path to my Desktop
desktop = pathlib.Path.home() / 'Desktop'
# Create a new folder
new_folder = pathlib.Path('/Users/m_a_t/Desktop/codingnomads')

# Filter for screenshots only
for x in desktop.iterdir():
    if x.is_file() and x.suffix == '.png':
        try:
            if not new_folder.exists():
                new_folder.mkdir()
                shutil.move(x, new_folder)
        except FileExistsError as err:
            print('FileExists')
# Create a new path for each file

# Move the screenshot there
