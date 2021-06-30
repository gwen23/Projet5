import mysql.connector
from DbCreation import DbCreate


class Connection:
    def __init__(self):
        self.DbCreate = DbCreate()


class Menu:

    def __init__(self):
        self.answer = ["New choice", "Quit", "Consult"]
        self.next_step = []

    def menu(self):
        ml = Program()

        while True:
            print("Choose a new category : 0 \n"
                  "Quit                  : 1 \n"
                  "Consult archived data : 2 \n")
            next_step = input("What do you want to do?")
            try:
                str(next_step)
                if next_step == "0":
                    ml.category_choice()
                    ml.show_products(c_choice)
                    ml.show_substitutes(c_choice, p_choice)
                    ml.an_other_choice()
                if next_step == "1":
                    print("Goodbye!")
                    exit(1)
                if next_step == "2":
                    ml.show_saved_choices()
            except ValueError:
                print("You must choose between 0, 1 and 2")


class Program:
    mn = Menu()
    c_choice = None
    p_choice = None

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root',
                                           password='',
                                           host='localhost',
                                           database='projet5')
        self.cursor = self.cnx.cursor()
        choices = []
        self.category_id = choices
        self.c_choices = None
        self.p_choices = None
        self.answer = ["Yes", "No"]

    def category_choice(self):
        query = 'SELECT idcategories, category_name FROM categories;'
        self.cursor.execute(query)
        c_choices = []
        print("Please make a selection ! ")
        for idcategories, category_name in self.cursor:
            print('{} : {}'.format(idcategories, category_name))
            c_choices.append(idcategories)
        while True:
            c_choice = input("Your choice:")
            try:
                int(c_choice)
            except ValueError:
                print("choose category")
                continue
            if int(c_choice) in c_choices:
                print("Good choice")
                print("You choose: category number {}:".format(c_choice))
                self.show_products(c_choice)
            else:
                print("choose a category !")

    def show_products(self, c_choice):
        p_choices = []
        query = 'SELECT category_id,' \
                ' idproducts,' \
                ' product_name' \
                ' FROM products' \
                ' WHERE category_id='+c_choice+'' \
                ' LIMIT 20 OFFSET 0;'
        self.cursor.execute(query)
        prod = self.cursor.fetchall()
        nutrition_grades = []
        for i in range(len(prod)):
            name = prod[i][2]
            category_id = prod[i][0]
            print("cat {}."
                  "   product_number {}."
                  "   name:{}".format(category_id,
                                      prod[i][1],
                                      name))

        while True:
            p_choice = input("Please choose a product number ")
            get_product_nutrition_grades = ('SELECT'
                                            ' product_nutrition_grades'
                                            ' FROM products WHERE'
                                            ' idproducts={};'
                                            .format(p_choice))
            self.cursor.execute(get_product_nutrition_grades)
            nutrition_grades.append(self.cursor.fetchone())

            for product_number in self.cursor:
                p_choices.append(product_number)
            try:
                int(p_choice)
                print("product number {} has been selected"
                      .format(p_choice))
                print("product_nutrition_grade is {}:"
                      .format(nutrition_grades))
                self.show_substitutes(p_choice, c_choice)

            except IndexError:
                print("You need to choose a good product number.")
                continue

            except ValueError:
                print("You need to choose a product number.")
                continue

    def show_substitutes(self, p_choice, c_choice):
        s_choices = []
        product_name = None
        query = 'SELECT category_id,' \
                ' idproducts,' \
                ' product_name,' \
                ' product_nutrition_grades,' \
                ' product_stores,' \
                ' product_link' \
                ' FROM products WHERE ' \
                'category_id='+c_choice+' ORDER BY product_nutrition_grades' \
                                        ' LIMIT 20;'
        self.cursor.execute(query)
        subst = self.cursor.fetchall()
        for i in range(len(subst)):
            product_number = subst[i][1]
            product_name = subst[i][2]
            product_nutrition_grades = subst[i][3]
            product_stores = subst[i][4]
            product_link = subst[i][5]
            if s_choices is None:
                print("There is no substitute")
            else:
                print("number {}: {}, with a '{}' nutrition_grade. \n "
                      "          can be found in store(s): {}, \n"
                      "           for more information follow this link: {}"
                      .format(product_number,
                              product_name,
                              product_nutrition_grades,
                              product_stores,
                              product_link))
        while True:
            s_choice = int(input("Please choose a substitute number:"))
            try:
                int(s_choice)
                print("product number {} : {} has been selected"
                      " as substitute.".format(s_choice, product_name))
                break
            except IndexError:
                print("You need to choose a good substitute number.")

                continue

            except ValueError:
                print("You need to choose a subtsitute number.")
                print(19)
                continue

        save = ()
        while save not in ["Yes", "No"]:
            save = input("Do you want to save your choice? Yes or No")

        if save == "Yes":
            query = ('INSERT into substitutes (product_id, substitute_id) '
                     'VALUES ({}, {})'.format(p_choice, s_choice))
            self.cursor.execute(query)
            self.cnx.commit()
            print("Choice recorded.")
            mn.menu()

        if save == "No":
            mn.menu()

    def show_saved_choices(self):
        query = 'SELECT ' \
                ' s.product_id as product_id,' \
                ' p1.product_name as product_name,' \
                ' p1.product_nutrition_grades as product_nutrition_grade,' \
                ' p1.product_link as product_link,' \
                ' p1.product_stores as product_stores, ' \
                ' s.substitute_id as substitute_id, ' \
                ' p2.product_name as substitute_name, ' \
                ' p2.product_nutrition_grades as substitute_nutrition_grade,' \
                ' p2.product_link as substitute_link, ' \
                ' p2.product_stores as substitute_stores ' \
                ' FROM `substitutes` as s ' \
                ' INNER JOIN `products` as p1 ' \
                ' ON s.product_id = p1.idproducts ' \
                ' INNER JOIN `products` as p2 ' \
                ' ON s.substitute_id = p2.idproducts ' \
                ' ;'

        self.cursor.execute(query)
        subst = self.cursor.fetchall()

        for i in range(len(subst)):
            substitute_id = subst[i][5]
            substitute_name = subst[i][6]
            product_id = subst[i][0]
            product_name = subst[i][1]
            print("(product_id {}/ {}) replaced by"
                  " (substitute_id/name : {}/{})"
                  .format(product_id, product_name,
                          substitute_id, substitute_name))


if __name__ == "__main__":
    c_choice = None
    p_choice = None
    mn = Menu()
    mn.menu()
    ml = Program()
    ml.category_choice()
    ml.show_products(c_choice)
    ml.show_substitutes(c_choice, p_choice)
