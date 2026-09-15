# pgPython

Проект подключается к PostgreSQL из Python и выводит все строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

![Вывод в консоли](screenshot_console.png)
![Таблица в pgAdmin](screenshot_pgadmin.png)

## app2.py (будет добавлен позже)
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.

![Вывод в консоли](screenshot_console2.png)