import sqlite3

sqlite_file = 'tweet_db.sqlite'
table_name1 = 'trend_and_tweet'
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE trend_and_tweet (
               id integer primary key autoincrement,
               timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
               trend varchar(50),
               tweet_id integer,
               tweet varchar(160))''')
cursor.execute("CREATE UNIQUE INDEX tweet_id on trend_and_tweet (tweet_id)")
# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
