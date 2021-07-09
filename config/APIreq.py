#! /usr/bin/env python3
# coding: utf-8

import mysql.connector
import requests
from constants import CATEGORIES, PRODUCTS_NUMBERS


class DataCollect:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',
                                           password='',
                                           host='localhost',
                                           database='projet5')
        self.cursor = self.cnx.cursor(buffered=True)

    def add_category(self):
        for element in CATEGORIES:
            add_cat = f"INSERT INTO categories (category_name)" \
                      f" VALUES ('{element}');"
            print(add_cat)
            try:
                self.cursor.execute(add_cat)
                self.cnx.commit()
            finally:
                pass

    def add_product(self):
        query = 'SELECT * FROM categories;'
        self.cursor.execute(query)
        for (id, name) in self.cursor.fetchall():
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
            req = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
                               params=payload)
            prod_req = req.json()
            data_prod = prod_req.get('products')

            for product in data_prod:
                i = 1
                if i < 101:
                    try:
                        name = product['product_name_fr']
                        nutrition_grades = product['nutrition_grade_fr']
                        link = product['url']
                        stores = product['stores']
                        cat_id = id
                        add_prod = f"INSERT INTO products" \
                                   f" (product_name," \
                                   f" product_nutrition_grades," \
                                   f" product_link," \
                                   f" product_stores," \
                                   f" category_id)" \
                                   f" VALUES" \
                                   f" ('{name}'," \
                                   f" '{nutrition_grades}'," \
                                   f" '{link}'," \
                                   f" '{stores}'," \
                                   f" '{cat_id}');"

                        try:
                            self.cursor.execute(add_prod)
                            self.cnx.commit()

                        except mysql.connector.Error as err:
                            print(err)
                    except KeyError:
                        pass
                i = i+1

        self.cursor.close()


if __name__ == "__main__":
    dc = DataCollect()
    dc.add_category()
    dc.add_product()
