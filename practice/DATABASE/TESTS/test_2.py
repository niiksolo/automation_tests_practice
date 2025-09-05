import sqlite3
import pytest


def test_db(db):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Album;')
    album = cursor.fetchall()
    print(album)
    assert len(album) > 0
    album_titles = [row [1] for row in album]
    assert 'For Those About To Rock We Salute You' in album_titles  #Если хочешь проверить, что конкретное название есть в списке:
    assert len(album) == 347, "Неверное количество альбомов в таблице"
    for row in album:
        assert isinstance(row[1], str), "Название альбома не строка"