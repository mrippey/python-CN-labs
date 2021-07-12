# Move the code you previously wrote to calculate
# how many seconds are in a year into this file.
# Then execute it as a script and print the output to your console.
from datetime import timedelta

year = timedelta(days=365)
print(year.total_seconds())