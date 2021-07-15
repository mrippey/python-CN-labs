# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

p = pathlib.Path('/Users/m_a_t/Documents/')

iterate_through_folders = [f for f in p.iterdir() if p.is_dir()]

for x in p.rglob('*'):
    print(f'File name: {x.name}')