<<<<<<< HEAD
import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

cur.execute("SELECT Название, Исполнитель FROM tracks;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
=======
import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

cur.execute("SELECT Название, Исполнитель FROM tracks;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
>>>>>>> 1ea581b9bff6a0fb861f55c4e488ac74c51d349e
conn.close()