import sqlite3
import pytest
import os

def test_db_structure(db):
    cursor = db.cursor()
    # Получаем все таблицы
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) > 0, "В базе нет таблиц"

    print("\nСписок таблиц:")
    for (table_name,) in tables:
        print(f"Таблица: {table_name}")

        # Получаем названия столбцов
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1;")
        columns = [desc[0] for desc in cursor.description]
        print("  Столбцы:", columns)

        # Получаем одну строку данных (если есть)
        row = cursor.fetchone()
        if row:
            print("  Пример данных:", row)
        else:
            print("  В таблице нет данных")





