import pandas as pd
import sqlite3
print("yay :)")
database = 'basketball.sqlite'
conn = sqlite3.connect(database)

joined_players = pd.read_sql("""SELECT pa.DISPLAY_FIRST_LAST AS player_name,
                                t.full_name AS team_name
                                FROM Player_Attributes pa
                                INNER JOIN Team t
                                ON pa.TEAM_ID = t.id
                                LIMIT 20
                                                                    """, conn)

print(joined_players)