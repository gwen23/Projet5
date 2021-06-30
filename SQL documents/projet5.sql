CREATE TABLE IF NOT EXISTS `categories` (
    `idcategories` smallint NOT NULL,
    `category_name` varchar(25) NOT NULL,
    PRIMARY KEY (`idcategories`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `products` (
    `idproducts` int NOT NULL AUTO_INCREMENT,
    `product_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `product_nutrition_grades` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `product_link` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `product_stores` text,
    `product_description` text NOT NULL,
    `category_id` int NOT NULL,
    PRIMARY KEY (`idproducts`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `substitutes` (
    `product_id` int NOT NULL,
    `substitute_id` int NOT NULL,
    KEY `product_id_idx` (`product_id`),
    KEY `substitute_id_idx` (`substitute_id`),
    CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`idproducts`),
    CONSTRAINT `substitute_id` FOREIGN KEY (`substitute_id`) REFERENCES `products` (`idproducts`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

