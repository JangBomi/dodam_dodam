import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT * FROM dodamweb_book_info LIMIT 0,10")
rows = cur.fetchall()
cols = [column[0] for column in cur.description]

conn.close()
# print(cols)
# print(rows)
for i in range(10):
    print(rows[i][2])