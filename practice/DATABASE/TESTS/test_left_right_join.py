import sqlite3


def test_left_join(db):
    cursor = db.cursor()
    cursor.execute('''SELECT Track.Name,Genre.Name
                   FROM Genre
                   LEFT JOIN Track
                   ON Genre.GenreId = Track.GenreId
                   ''')
    results = cursor.fetchall()



def test_right_join(db):
    cursor = db.cursor()
    cursor.execute('''SELECT Genre.Name , Track.Name
    FROM Track
    RIGHT JOIN Genre
    ON Genre.GenreId == Track.GenreId
    LIMIT 5''')
    RIGHT = cursor.fetchall()
    print(RIGHT)

def test_training_join(db):
    cursor = db.cursor()
    cursor.execute('''SELECT Customer.FirstName , Customer.LastName , Invoice.InvoiceDate, Invoice.BillingCity
    FROM Customer
    LEFT JOIN Invoice
    ON Customer.CustomerId == Invoice.CustomerId
    LIMIT 5''' )
    result = cursor.fetchall()
    print(result)