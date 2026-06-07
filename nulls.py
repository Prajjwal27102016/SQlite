import sqlite3
import pandas as pd
database = 'basketball.sqlite'
conn = sqlite3.connect(database)
print("Done :)")

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables.head())

Player_Salary = pd.read_sql("""SELECT * 
                      FROM Player_Salary;""",conn)

Player_Salary.info()