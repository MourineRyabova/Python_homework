# Python_homework
### Проект по созданию асинхронного приложения, взаимодействующего с базой данных SQLite

Описание структуры:
1. main.py - основной файл с подключением базы и бэкендом на базе FastAPI
2. pd_tables_create.py - файл с функциями, заполняющими таблицы в базе данных
3. classes.py - файл с классами pydantic
4. stores_addresses.csv и items.csv - таблицы - заготовки для загрузки синтетических данных в базу
5. requirements.txt - список зависимостей, использованных в проекте


### Проблема:
В коде создаю базу данных toys.db. Она ложится в ту же папку, что и проект. Данными наполняется. Из датагрипа вижу ее. Но когда я запускаю приложение с помощью  uvicorn main:app --port 8000 --reload, на интерфейсе (http://127.0.0.1:8000/docs#/) как будто пусто.

### Вопрос
В чем может быть проблема? Из-за чего приложение не видит базу?
