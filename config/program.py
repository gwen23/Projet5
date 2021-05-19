import mysql.connector
import constants
import Classes
import database
from DbCreation import DbCreate

import mysql.connector

from constants import CATEGORIES
from Classes import Category, Product
from APIreq import DataCollect
# se connecter à la base de données
# vider bdd et la recréer ( DbCreate )


class Connection:
    def __init__(self):
        self.DbCreate = DbCreate()


# menu principal
# quitter le programme ou continuer  Q
# choisir une catégorie              1
# accéder a la bdd utilisateur       2
class Program:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='projet5', password='projet5', host='localhost', database='projet5')
        self.cursor = self.cnx.cursor()
        self.category_id = None

    def category_choice(self):
        choice = None
        query = 'SELECT idcategories, category_name FROM categories;'
        self.cursor.execute(query)
        category_dict = {}
        print(" Please make a selection ! ")
        for i in range(len(CATEGORIES)):
            for idcategories, category_name in self.cursor:
                print('{} : {}'.format(idcategories, category_name))
            while True:
                try:
                    self.category_id = int(input("Your choice:"))
                    choice = category_dict[self.category_id]
                except ValueError:
                    print("choose a category !")
                except KeyError:
                    if i in range(len(CATEGORIES)):
                        print("Good choice")
                        break
                    else:
                        print("choose a category !")
                    print("You choose: category number {}:".format(self.category_id))

    def show_products(self):
        query = 'SELECT idproducts, product_name FROM products WHERE category_id= {}'.format(self.category_id)
        self.cursor.execute(query)
        prod = self.cursor.fetchall()
        print(query)
        for i in range(len(prod)):
            while True:
                try:
                    self.idproducts.choice = int(input("Please choose a product_id"))
                    get_nutriscore = ('SELECT product_nutriscore FROM products WHERE'
                                      ' idproducts= {} AND category_id= {}'.format
                                      (self.idproducts.choice, self.category_id))
                    print(product_nutriscore)
                except:
                    pass



if __name__ == "__main__":
    ml = Program()
    ml.category_choice()
    #ml.show_products()


# créer la boucle proposant les catégories
# demander le choix de l'utilisateur avec les conditions  1 à 5
# true : afficher la catégorie choisie ou revenir au choix de la catégorie
# false : afficher "insérer un chiffre correspondant à une des catégories proposées"


# une fois la catégorie choisie:
# afficher liste des produits de la catégorie
# choisir un produits parmi ceux proposés
# proposer une liste de produits similaires avec un meilleur nutrition_grade ( 10 par page )
# une fois le substitut proposer de l'enregistrer dans la base de données utilisateur

# liste des situations ( meilleur nutG, pas de meilleur nutG, annulation choix produit ... )
# retour au menu principal
