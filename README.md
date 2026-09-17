# pgPython

Проект подключается к PostgreSQL из Python и выводит строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

![Вывод в консоли](screenshot_console.png)
![Таблица в pgAdmin](screenshot_pgadmin.png)

## app2.py
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.

![Вывод app2.py](screenshot_console2.png)

## app3.py
Выполняет запрос `SELECT Название, Исполнитель, Год FROM tracks;` и выводит три столбца: название, исполнитель, год.

![Вывод app3.py](screenshot_console3.png)

## app4.py
Выполняет запросы с WHERE и ORDER BY (фильтрация по исполнителю, году, длительности; сортировка по названию).

![Вывод app4.py](screenshot_console4.png)

## app5.py
Выполняет запрос `SELECT Название, Год FROM tracks WHERE Год > 2015;` и выводит только название и год для треков после 2015 года.

![Вывод app5.py](screenshot_console5.png)

## app6.py
Запрашивает у пользователя название, исполнителя, год и длительность, добавляет новую строку в таблицу `tracks` через `INSERT` и выводит всё содержимое таблицы.

![Вывод app6.py](screenshot_pgadmin6.png)