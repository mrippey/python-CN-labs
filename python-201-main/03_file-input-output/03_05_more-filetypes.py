# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import csv
import pathlib

path_to_csv = pathlib.Path("/Users/m_a_t/Documents/CodingNomads/labs/python-201-main/03_file-input-output/file-counter/filecounts.csv")

file_types_to_record  = ["Folder", "CSV", "MD", "PNG"]

with open(path_to_csv, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=file_types_to_record)
    counts = list(reader)

print(counts)