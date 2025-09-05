import sqlite3

def test_artist_limit():
    conn = sqlite3.connect('../BASE/Chinook_Sqlite.sqlite')  # открываем базу
    cursor = conn.cursor()
    cursor.execute('SELECT Name FROM Artist LIMIT 7;')
    artists = cursor.fetchall()
    conn.close()
    assert len(artists) > 0

    artists_name = [a[0] for a in artists]
    assert 'AC/DC' in artists_name
