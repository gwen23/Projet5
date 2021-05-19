import mysql.connector
import requests
import json
from constants import CATEGORIES, PRODUCTS_NUMBERS


class DataCollect:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='projet5', password='projet5', host='localhost', database='projet5')
        self.cursor = self.cnx.cursor(buffered=True)

    def add_category(self):
        for element in CATEGORIES:
            add_cat = f"INSERT INTO categories (category_name) VALUES ('{element}');"
            print(add_cat)
            try:
                self.cursor.execute(add_cat)
                self.cnx.commit()
            finally:
                pass

    def add_product(self):
        query = 'SELECT * FROM categories;'
        self.cursor.execute(query)
        for (id, name) in self.cursor:
            print(id, name)
            payload = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': name,
                'tagtype_1': 'nutrition_grade',
                'tag_contains_1': 'contains',
                'page_size': PRODUCTS_NUMBERS,
                'json': 'true',
            }
            req = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
            prod_req = req.json()
            data_prod = prod_req.get('products')
            # NE PAS TOUCHER AU DESSUS

            for element in CATEGORIES:
                for product in data_prod:
                    print(product)
                    name = product['product_name_fr']
                    nutrition_grades = product['nutrition_grade_fr']
                    link = product['url']
                    stores = product['stores']
                    cat_id = id

                    print(7)
                    add_prod = f"INSERT INTO products (product_name, product_nutrition_grades," \
                               f" product_link, product_stores, category_id)" \
                               f" VALUES ('{name}', '{nutrition_grades}', '{link}', '{stores}', '{cat_id}');"
                    print(add_prod)
                    try:
                        self.cursor.execute(add_prod)
                        print(8)
                        self.cnx.commit()
                        print(9)
                    except mysql.connector.Error as err:
                        print(err)

        self.cursor.close()


if __name__ == "__main__":
    dc = DataCollect()
    dc.add_category()
    dc.add_product()
