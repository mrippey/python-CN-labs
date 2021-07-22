# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlite3 


try:
    sqlite3conn = sqlite3.connect('somedb.db')
    cursor = sqlite3conn.cursor()
    print('connection successful')

    fetch_records = cursor.fetchall()
    cursor.close()

except sqlite3.Error as err:
    print('Error!: {err}')

else:
    print('Database creation and connection successful, awaiting next command')