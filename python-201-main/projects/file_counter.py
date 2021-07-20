# Add the code for the file counter script that you wrote in the course.

from pathlib import Path

from collections import Counter
# Find the path to my Desktop
#desktop = Path.home() / 'Desktop'
# Create a new folder
#new_folder = Path('/Users/m_a_t/Desktop/codingnomads')
def file_search(file_pth):
    file_pth = Path(file_pth)
# Filter for screenshots only
    for img in file_pth.iterdir():
        if img.is_file() and img.suffix == '.jpg':
            print(f"Files ending in '.jpg': {img}")
            print()
    file_ext_counter = (path.suffix for path in file_pth.iterdir() if path.is_file() and path.suffix)
    return f'Count of file extensions in {file_pth}: {dict(Counter(file_ext_counter))}'

print(file_search('/Users/m_a_t/Desktop'))