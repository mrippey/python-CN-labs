# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

right_now = datetime.now()

current_time_readable = right_now.strftime("%H:%M:%S")

print(current_time_readable)