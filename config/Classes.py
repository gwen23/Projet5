#! /usr/bin/env python3
# coding: utf-8

class Category:
    """OpenFoodFacts Categories"""
    def __init__(self, idcategories, category_name, url):
        self.idcategories = idcategories
        self.category_name = category_name
        self.url = url


class Product:
    """OpenFoodFacts Products"""
    def __init__(self,
                 idproducts,
                 product_name,
                 product_nutrition_grades,
                 product_link,
                 product_stores,
                 product_description,
                 category_id):
        self.idproducts = idproducts
        self.product_name = product_name
        self.product_nutrition_grades = product_nutrition_grades
        self.product_link = product_link
        self.product_stores = product_stores
        self.product_description = product_description
        self.category_id = category_id
