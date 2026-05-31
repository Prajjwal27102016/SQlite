import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data sucessfully')

import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables.head())

matches = pd.read_sql("""SELECT * 
                      FROM Match;""",conn)

matches.info()