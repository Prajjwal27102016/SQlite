import sqlite3
database = 'basketball.sqlite'
conn = sqlite3.connect(database)
print('Opened data sucessfully')

import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables.head())

Teams = pd.read_sql("""SELECT * 
                      FROM Team;""",conn)

Teams.info()

Player_Salary = pd.read_sql("""SELECT * 
                      FROM Player_Salary;""",conn)

Player_Salary.info()
