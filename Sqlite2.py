import sqlite3
import pandas as pd
database = 'database.sqlite'
conn = sqlite3.connect(database)

print('Opened database successfully')

tables = pd.read_sql("""

SELECT name

FROM sqlite_master

WHERE type='table';

""", conn)


#sqlite_master is a special system table that stores metadata about all tables, indexes, and views in the database.WHERE type='table' filters only the tables.SELECT name returns just the table names.

print(tables)

df_player = pd.read_sql("SELECT * FROM Bowling_Style;", conn)

# Show the first few rows

print(df_player.head(20))