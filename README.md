# pgPython

Проект подключается к PostgreSQL из Python и выводит все строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

![Вывод в консоли](<img width="1465" height="937" alt="image" src="https://github.com/user-attachments/assets/ea63bd42-d742-4a26-886f-e2766ee8bc1f" />
)
![Таблица в pgAdmin](screenshot_pgadmin.png)

## app2.py (будет добавлен позже)
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.

![Вывод в консоли](screenshot_console2.png)
