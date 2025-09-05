import sqlite3

def test_update(db):
    cursor = db.cursor()
    cursor.execute("UPDATE Employee SET LastName='Solo',FirstName='Nik' WHERE EmployeeId=1")
    db.commit()
    cursor.execute('SELECT LastName, FirstName FROM Employee WHERE EmployeeId=1')
    row = cursor.fetchone()
    assert row == ('Solo', 'Nik')

