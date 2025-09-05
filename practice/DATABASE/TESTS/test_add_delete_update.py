import sqlite3

def test_box(db):
    cursor = db.cursor()
    # удаляем если есть повторы
    cursor.execute("DELETE FROM Artist WHERE Name = 'Бумбокс'")
    db.commit()
    # Добовляю в таблицу
    cursor.execute("INSERT INTO Artist (Name) VALUES ('Бумбокс')")
    db.commit()
    #Проверяю что добавил
    cursor.execute("SELECT Name FROM Artist WHERE Name='Бумбокс'")
    result = cursor.fetchall()
    assert len(result) == 1
    assert result[0][0] == 'Бумбокс'
    # Удаляю
    delete = cursor.execute("DELETE FROM Artist WHERE Name='Бумбокс'")
    db.commit()
    #Проверяю что удалил
    cursor.execute("SELECT Name FROM Artist WHERE Name='Бумбокс'")
    delete = cursor.fetchall()
    assert len(delete) == 0




def test_artist_bymboks(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Artist WHERE ArtistId >274' )
    art =cursor.fetchall()
    print(art)

def test_delete_column(db):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Artist WHERE Name='Бумбокс'")
    db.commit()


