import sqlite3

def test_pragma(db):
    cursor = db.cursor()
    cursor.execute("PRAGMA table_info (Artist)") #получить названия столбцов в таблице
    art = cursor.fetchall()
    print(art)

    # еще полезный вариант использования
    # Включить или отключить проверку внешних ключей
    # foreign_keys = ON; / OFF;

