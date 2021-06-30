import mysql.connector

DB_CATEGORIES = 'categories'
DB_PRODUCTS = 'products'
DB_SUBSTITUTES = 'substitutes'


class DbCreate:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',
                                           password='',
                                           host='localhost',
                                           database='projet5')
        self.cursor = self.cnx.cursor()

    def drop_tables(self):
        self.cursor.execute(
            "DROP TABLES IF EXISTS categories, products, substitutes;"
        )

    def tables_creation(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS`categories` ("
            "  `idcategories` smallint NOT NULL AUTO_INCREMENT,"
            "  `category_name` varchar(255) NOT NULL,"
            "  PRIMARY KEY (`idcategories`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        )

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS`products` ("
            "  `idproducts` int NOT NULL AUTO_INCREMENT,"
            "  `product_name` varchar(255) CHARACTER SET"
            " utf8 COLLATE utf8_general_ci NOT NULL,"
            "  `product_nutrition_grades` char(1) CHARACTER SET"
            " utf8 COLLATE utf8_general_ci NOT NULL,"
            "  `product_link` text CHARACTER SET utf8 COLLATE"
            " utf8_general_ci NOT NULL,"
            "  `product_stores` text,"
            "  `category_id` text NOT NULL,"
            "  PRIMARY KEY (`idproducts`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        )

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS`substitutes` ("
            "  `product_id` int NOT NULL,"
            "  `substitute_id` int NOT NULL,"
            "  KEY `product_id_idx` (`product_id`),"
            "  KEY `substitute_id_idx` (`substitute_id`),"
            "  CONSTRAINT `product_id` FOREIGN KEY (`product_id`)"
            " REFERENCES `products` (`idproducts`),"
            "  CONSTRAINT `substitute_id` FOREIGN KEY (`substitute_id`)"
            " REFERENCES `products` (`idproducts`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        )


if __name__ == "__main__":
    db = DbCreate()
    db.drop_tables()
    db.tables_creation()
