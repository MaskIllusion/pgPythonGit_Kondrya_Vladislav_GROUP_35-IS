import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="admin"
)

cur = conn.cursor()

#cur.execute("SELECT * FROM tracks WHERE Исполнитель = 'Linkin Park';")
#cur.execute("SELECT * FROM tracks WHERE Год = 2017;")
#cur.execute("SELECT * FROM tracks WHERE Год < 2000;")
#cur.execute("SELECT * FROM tracks WHERE Год > 2015;")
#cur.execute("SELECT * FROM tracks WHERE Длительность > 200;")
#cur.execute("SELECT * FROM tracks WHERE Длительность > 300;")
#cur.execute("SELECT * FROM tracks WHERE Длительность < 170;")
#cur.execute("SELECT * FROM tracks WHERE Длительность >= 200;")
#cur.execute("SELECT * FROM tracks WHERE Исполнитель = 'Король и Шут';")

cur.execute("SELECT * FROM tracks ORDER BY Название ASC;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()