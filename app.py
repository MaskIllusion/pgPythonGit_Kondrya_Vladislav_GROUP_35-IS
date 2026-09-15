# Подключаем библиотеку psycopg для работы с PostgreSQL
import psycopg

# Открываем соединение с базой данных
conn = psycopg.connect(
    host="localhost",      # База находится на этом же компьютере
    dbname="tracks_bd",    # Имя нашей базы данных
    user="postgres",       # Стандартный пользователь
    password="admin"       # Ваш пароль (с маленькой буквы!)
)

# Создаем курсор — "ручку" для отправки SQL-запросов
cur = conn.cursor()

# Отправляем SQL-запрос: выбрать все столбцы из таблицы tracks
cur.execute("SELECT * FROM tracks;")

# Забираем все строки результата в список
rows = cur.fetchall()

# Перебираем строки в цикле и выводим каждую на экран
for row in rows:
    print(row)

# Закрываем курсор и соединение с базой
cur.close()
conn.close()