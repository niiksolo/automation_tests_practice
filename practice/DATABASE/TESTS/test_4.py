import os
import sqlite3
import pytest

def test_BASE(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM customer')  #  выбрал всю таблицу Customer
    customer = cursor.fetchall()
    assert len(customer) > 0,"Таблица Customer пуста"
    cursor.execute("SELECT 1 FROM Customer LIMIT 1;")  # проверить, что таблица содержит хотя бы одну запись
    assert cursor.fetchone() is not None, "Таблица Customer пуста"

def test_BASE2(db):
    cursor = db.cursor()
    cursor.execute('SELECT GenreId FROM Genre;')  # выбрал один столбец из таблицы Genre
    GenreId = cursor.fetchall()
    assert GenreId is not None
    assert len(GenreId) == 25

def test_BASE3(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Employee LIMIT 5;')  # верни 5 строк из таблицы employee
    Employee = cursor.fetchall()
    print(Employee)

def test_BASE4(db):
    cursor = db.cursor()
    cursor.execute('SELECT PlaylistId FROM PlaylistTrack')
    rows = cursor.fetchall()
    all_int = all(isinstance(row[0],int) for row in rows)   # все в столбце является цифрами
