import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

# Выводим всё, что есть в таблице
cur.execute("SELECT * FROM tracks;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Запрашиваем данные у пользователя
nazvanie = input("Название: ")
ispolnitel = input("Исполнитель: ")
god = int(input("Год: "))
dlitelnost = int(input("Длительность (сек): "))

# Вставляем новую строку
cur.execute(
    "INSERT INTO tracks (Название, Исполнитель, Год, Длительность) VALUES (%s, %s, %s, %s);",
    (nazvanie, ispolnitel, god, dlitelnost)
)

# ФИКСИРУЕМ ИЗМЕНЕНИЯ — вот это важно
conn.commit()

print("Строка добавлена!")

cur.close()
conn.close()