import mysql.connector

from mysql.connector import errorcode


try:
    cnx = mysql.connector.connect(user='root', password='Kepler@123b', host='127.0.0.1', database='projet5')
    cursor = cnx.cursor()

    request = 'SELECT * from https://fr.openfoodfacts.org/'
    cursor.execute(request)
    category_list = cursor.fetchall()
    products_list = cursor.fetchall()
    substitutes_list = cursor.fetchall()

    for category in categories:
        print('category_name : {}'.format(category[1]))

    for product in products:
        print('product_name : {}'.format(products[1]))
        print('product_nutrition_grades : {}'.format(products[2]))
        print('product_link : {}'. format(products[3]))
        print('product_stores : {}'. format(products[4]))
        print('product_description : {}'. format(products[5]))
        print('category_id : {}'. format(products[6]))

    for substitute in substitutes:
        print('product_id : {}'.format(products[1]))
        print('subsitute_id : {}'.format(products[2]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
