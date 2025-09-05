import sqlite3

def test_group_by_having(db):
    cursor = db.cursor()
    cursor.execute('''
    SELECT                      
        BillingCountry, 
        ROUND(SUM(Total), 2) as TotalSales 
    FROM Invoice
    GROUP BY BillingCountry 
    HAVING SUM(Total) > 100
    ORDER BY TotalSales DESC LIMIT 3 ''')
    count = cursor.fetchall()
    print(count)
    assert len(count) > 0
    # СУММА ПРОДАЖ ПО СТРАНАМ  у кого продажи больше 100 и отсортировали от наибольшей суммы ее и отсортировали ТОП 3 страны