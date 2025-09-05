import sqlite3
import pytest

def test_chinook(db):
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем FK проверки
    cursor.execute("BEGIN")

    try:
        # FirstName не может быть NULL
        with pytest.raises(sqlite3.IntegrityError):
            cursor.execute("""
                INSERT INTO Customer (LastName, FirstName, Email, SupportRepId)
                VALUES ('Doe', NULL, 'notnull@example.com', 3)
            """)

        # вставка Invoice с несуществующим CustomerId
        with pytest.raises(sqlite3.IntegrityError):
            cursor.execute("""
                INSERT INTO Invoice (CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingCountry, Total)
                VALUES (999999, '2025-01-01 00:00:00', 'Fake St', 'Nowhere', 'Noland', 10.0)
            """)

        # пытаемся вставить дубликат Email
        try:
            cursor.execute("""
                INSERT INTO Customer (FirstName, LastName, Email, SupportRepId)
                VALUES ('John', 'Doe', 'duplicate@example.com', 3)
            """)
            cursor.execute("""
                INSERT INTO Customer (FirstName, LastName, Email, SupportRepId)
                VALUES ('Jane', 'Smith', 'duplicate@example.com', 3)
            """)
            print("❌ UNIQUE ограничение не сработало — в базе Chinook нет такого ограничения")
        except sqlite3.IntegrityError:
            print("✅ UNIQUE ограничение сработало")

        # пробуем вставить отрицательное значение Total (в Chinook CHECK нет)
        try:
            cursor.execute("""
                INSERT INTO Invoice (CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingCountry, Total)
                VALUES (1, '2025-01-01 00:00:00', 'Test', 'City', 'Country', -100.0)
            """)
            print("❌ CHECK ограничение не сработало — отрицательное значение прошло")
        except sqlite3.IntegrityError:
            print("✅ CHECK ограничение сработало")

    finally:
        cursor.execute("ROLLBACK")

    # После rollback проверяем, что в базе нет вставленных записей
    cursor.execute("SELECT COUNT(*) FROM Customer WHERE Email IN ('notnull@example.com', 'duplicate@example.com')")
    count_customer = cursor.fetchone()[0]
    assert count_customer == 0, "В таблице Customer остались записи после rollback!"

    cursor.execute("SELECT COUNT(*) FROM Invoice WHERE BillingAddress='Test'")
    count_invoice = cursor.fetchone()[0]
    assert count_invoice == 0, "В таблице Invoice остались записи после rollback!"