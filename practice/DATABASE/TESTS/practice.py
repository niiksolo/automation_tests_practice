import sqlite3

def test_db(db):
    cursor = db.cursor()
    cursor.execute('''SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total)
                    FROM Customer
                    LEFT JOIN Invoice
                    ON Customer.CustomerId == Invoice.CustomerId
                    GROUP BY Customer.CustomerId''')
    test = cursor.fetchall()
    print(test)
    assert len(test) >0