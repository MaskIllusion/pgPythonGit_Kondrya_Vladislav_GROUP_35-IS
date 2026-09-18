# Импортируем модуль tkinter для создания окна, кнопок и подписей
from tkinter import *
# Импортируем модуль ttk для полей ввода и кнопки
from tkinter import ttk
# Импортируем модуль psycopg для подключения к PostgreSQL
import psycopg


# Это функция. Она выполнится, когда пользователь нажмёт кнопку «Добавить»
def save_track():
    # Берём текст из полей
    nazvanie = entry_name.get()
    ispolnitel = entry_artist.get()

    # Пробуем превратить год и длительность в числа
    try:
        god = int(entry_year.get())
        dlitelnost = int(entry_len.get())
    except ValueError:
        label["text"] = "Ошибка: год и длительность — числа"
        return

    # Открываем соединение с базой tracks_bd
    conn = psycopg.connect(
        host="localhost",
        dbname="tracks_bd",
        user="postgres",
        password="admin"
    )
    cur = conn.cursor()

    # Добавляем строку в таблицу tracks
    cur.execute(
        "INSERT INTO tracks (Название, Исполнитель, Год, Длительность) VALUES (%s, %s, %s, %s);",
        (nazvanie, ispolnitel, god, dlitelnost)
    )
    # Фиксируем изменения
    conn.commit()
    # Закрываем курсор и соединение
    cur.close()
    conn.close()

    # Пишем внизу окна, что трек добавлен
    label["text"] = "Добавлено: " + nazvanie


# Создаём главное окно программы
root = Tk()
root.title("Добавить трек")
root.geometry("280x300")

# Подпись и поле для Названия
ttk.Label(root, text="Название").pack(anchor=NW, padx=6, pady=2)
entry_name = ttk.Entry()
entry_name.pack(anchor=NW, padx=6, pady=2)

# Подпись и поле для Исполнителя
ttk.Label(root, text="Исполнитель").pack(anchor=NW, padx=6, pady=2)
entry_artist = ttk.Entry()
entry_artist.pack(anchor=NW, padx=6, pady=2)

# Подпись и поле для Года
ttk.Label(root, text="Год").pack(anchor=NW, padx=6, pady=2)
entry_year = ttk.Entry()
entry_year.pack(anchor=NW, padx=6, pady=2)

# Подпись и поле для Длительности
ttk.Label(root, text="Длительность").pack(anchor=NW, padx=6, pady=2)
entry_len = ttk.Entry()
entry_len.pack(anchor=NW, padx=6, pady=2)

# Кнопка «Добавить»
btn = ttk.Button(text="Добавить", command=save_track)
btn.pack(anchor=NW, padx=6, pady=6)

# Подпись внизу окна для вывода результата
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

# Запускаем окно
root.mainloop()