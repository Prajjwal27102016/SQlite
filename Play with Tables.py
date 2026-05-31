import sqlite3
database = "database.sqlite"
conn = sqlite3.connect(database)

print('opened data successfully')

import pandas as pd
tables=pd.read_sql(""" SELECT * 
                   FROM sqlite_master
                   WHERE type = 'table';""",conn)
print(tables)

matches=pd.read_sql(""" SELECT * 
                   FROM Match;""",conn)
matches.head


result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner
                        FROM Match
                        WHERE Season_Id == 9
                        GROUP BY Match_Winner
                        ORDER BY AVG(Win_Margin);""", conn)

print (result1)

result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
                        FROM Match
                        WHERE Season_Id == 9;""", conn)

print(result2)