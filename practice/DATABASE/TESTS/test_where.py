import sqlite3

def test_DB_where(db):
    cursor = db.cursor()
    cursor.execute ("SELECT name FROM sqlite_master WHERE type='table'")  #сиситемная таблица где хранятся данные обо всей базе
    table = cursor.fetchall()
    assert table is not None
    assert len(table) == 11
    print(table)

def test_limit(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Invoice LIMIT 3')  # первые три строчки из таблицы Invoice
    Invoice = cursor.fetchall()
    assert Invoice is not None
    print(Invoice)

def test_where(db):
    cursor = db.cursor()
    cursor.execute("SELECT Name FROM MediaType WHERE Name LIKE '%MPEG%'" ) # в столбце ищем по слову MPEG
    mpeg = cursor.fetchall()
    print(mpeg)

def test_where(db):
    cursor = db.cursor()
    cursor.execute("SELECT ArtistId FROM Album WHERE ArtistId >5")
    artistId = cursor.fetchall()
    print(artistId)

def test_where2(db):
    cursor = db.cursor()
    cursor.execute("SELECT ArtistId FROM Album WHERE ArtistId BETWEEN 1 AND 12")
    artistId = cursor.fetchall()
    print(artistId)

def test_distinct(db):
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT Name FROM Genre ")   # только уникальные имена
    name = cursor.fetchall()
    print(name)

def test_DESC(db):
    cursor = db.cursor()
    cursor.execute("SELECT ArtistId FROM Artist ORDER BY ArtistId DESC")   # с конца в начало дает список
    DESC = cursor.fetchall()
    print(DESC)

def test_COUNT(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(AlbumId) FROM Album ")   # с конца в начало дает список
    COUNT = cursor.fetchall()
    print(COUNT)
