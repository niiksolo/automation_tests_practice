import sqlite3

def test_inner_join(db):
    cursor = db.cursor()
    cursor.execute('''
        SELECT Album.Title, Artist.Name
        FROM Album
        INNER JOIN Artist 
        ON Album.ArtistId = Artist.ArtistId     
        LIMIT 5
    ''')
    result = cursor.fetchall()
    assert len(result) == 5
    print(result)