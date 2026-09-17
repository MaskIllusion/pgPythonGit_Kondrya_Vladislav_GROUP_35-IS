# pgPython

Проект подключается к PostgreSQL из Python и выводит все строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

Вывод в консоли (<img width="1163" height="920" alt="Снимок консоля" src="https://github.com/user-attachments/assets/b99511b7-09cc-4d3f-831a-8a3c3e40f720" />

Таблица в pgAdmin (<img width="1050" height="914" alt="Снимок БД" src="https://github.com/user-attachments/assets/d9b75fe0-382a-4031-8ac5-1b495f4356ae" />

## app2.py 
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.



Вывод в консоли (<img width="1275" height="905" alt="Снимок консоля 2" src="https://github.com/user-attachments/assets/f720b097-76b6-4f3a-a95b-0401b92931ed" />

## app3.py
Выполняет запрос `SELECT Название, Исполнитель, Год FROM tracks;` и выводит три столбца: название, исполнитель, год.

Вывод app3.py (<img width="1324" height="984" alt="Снимок консоля 3" src="https://github.com/user-attachments/assets/9422ded4-ef22-4999-94c7-01aac17ee588" />

## app4.py
Выполняет запросы с WHERE и ORDER BY (фильтрация по исполнителю, году, длительности; сортировка по названию).

![Вывод app4.py](screenshot_console4.png)

## app5.py
Выполняет запрос `SELECT Название, Год FROM tracks WHERE Год > 2015;` и выводит только название и год для треков после 2015 года.

![Вывод app5.py](screenshot_console5.png)


## app6.py
Запрашивает у пользователя название, исполнителя, год и длительность, добавляет новую строку в таблицу `tracks` через `INSERT` и выводит всё содержимое таблицы.

Вывод app6.py (<img width="1501" height="990" alt="screenshot_pgadmin6" src="https://github.com/user-attachments/assets/6a30e512-0482-4283-b57b-e590529be422" />
