# pgPython

Проект подключается к PostgreSQL из Python и выводит все строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

![Вывод в консоли](<img width="1163" height="920" alt="Снимок консоля" src="https://github.com/user-attachments/assets/b99511b7-09cc-4d3f-831a-8a3c3e40f720" />
)

![Таблица в pgAdmin](<img width="1050" height="914" alt="Снимок БД" src="https://github.com/user-attachments/assets/d9b75fe0-382a-4031-8ac5-1b495f4356ae" />
)

## app2.py (будет добавлен позже)
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.

![Вывод в консоли](screenshot_console2.png)
