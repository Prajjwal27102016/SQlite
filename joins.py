import numpy as np
import pandas as pd
import sqlite3
print("yay:)")

database = ''
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table'""", conn)

print(tables)

joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            INNER JOIN city ci
                            ON c.Country_Id == ci.Country_id""", conn)

print(joined_city)