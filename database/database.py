import mysql.connector


try:
    cnx = mysql.connector.connect(user='root',
                                  password='',
                                  host='localhost',
                                  database='projet5')
    cursor = cnx.cursor()

    request = 'SELECT * from categories, products, substitutes;'
    cursor.execute(request)
    category_list = cursor.fetchall()
    products_list = cursor.fetchall()
    substitutes_list = cursor.fetchall()
finally:
    pass
