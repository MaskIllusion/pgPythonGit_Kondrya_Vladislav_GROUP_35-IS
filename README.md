# pgPython

Проект подключается к PostgreSQL из Python и выводит все строки из таблицы `tracks`.

## app.py
Выполняет запрос `SELECT * FROM tracks;` и печатает все строки.

Вывод в консоли (<img width="1163" height="920" alt="Снимок консоля" src="https://github.com/user-attachments/assets/b99511b7-09cc-4d3f-831a-8a3c3e40f720" />

Таблица в pgAdmin (<img width="1050" height="914" alt="Снимок БД" src="https://github.com/user-attachments/assets/d9b75fe0-382a-4031-8ac5-1b495f4356ae" />

## app2.py 
Выполняет запрос `SELECT Название, Исполнитель FROM tracks;` и печатает только эти два столбца.

(screenshot_console2.png)

Вывод в консоли (<img width="1275" height="905" alt="Снимок консоля 2" src="https://github.com/user-attachments/assets/f720b097-76b6-4f3a-a95b-0401b92931ed" />

## app3.py
Выполняет запрос `SELECT Название, Исполнитель, Год FROM tracks;` и выводит три столбца: название, исполнитель, год.

Вывод app3.py (<img width="1324" height="984" alt="Снимок консоля 3" src="https://github.com/user-attachments/assets/9422ded4-ef22-4999-94c7-01aac17ee588" />
>>>>>>> 1ea581b9bff6a0fb861f55c4e488ac74c51d349e
