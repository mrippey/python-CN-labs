# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import csv
import pathlib

path_to_csv = pathlib.Path("/Users/m_a_t/Documents/CodingNomads/labs/python-201-main/03_file-input-output/file-counter/filecounts.csv")

with open(path_to_csv, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)