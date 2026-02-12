create a python project Youtube_manager.py using function



enumerate also help for indexing
formatted string (f"{}.")

<!-- now Youtube manager with database -->
Now import sqlite 3 to connect database with this 
cursor.execute('''
               CREATE TABLE IF NOT EXIST videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )''')
