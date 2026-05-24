import sqlite3
import pandas as pd
database = 'basketball.sqlite'
conn = sqlite3.connect(database)

print("Done :)")

tables = pd.read_sql("""

SELECT name

FROM sqlite_master

WHERE type='table';

""", conn)

print(tables)

df_player = pd.read_sql("SELECT * FROM Team;", conn)
print(df_player.head(15))
