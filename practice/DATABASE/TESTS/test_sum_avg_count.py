import sqlite3

def test_count(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT
            COUNT(*) as line_count,
            SUM(UnitPrice * Quantity) as total_sales,
            AVG(UnitPrice * Quantity) as average_line_total
        FROM InvoiceLine
    """)
    result = cursor.fetchone()
    line_count, total_sales, average_line_total = result

    assert line_count > 0 #количество строк (InvoiceLine)
    assert total_sales > 0 #общая сумма
    assert average_line_total > 0 #средняя сумма строки
    assert average_line_total <= total_sales
    print(result)
