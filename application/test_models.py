
import unittest
from models import Category
from models import User
class TestCRUDMethods(unittest.TestCase):
    """ Tests methods from the various model classes in the models module """

    def setUp(self):
        self.user = User("Adri Morg", "adri.morg", "password")

    def test_add_category(self):
        """ Tests adding a new category """
        self.assertEqual(self.user.add_category(None), "None input")
        self.assertEqual(self.user.add_category(" "), "Blank input")
        self.assertEqual(self.user.add_category("shortname"),
                         "Category name should than 2 characters")
        self.assertEqual(self.user.add_category
                         ("long name long name long name long name long name long name long name"),
                         "Category name should than 2 characters")
        self.assertEqual(self.user.add_category("Things I should do before I am 30 years old"),
                         "Category added")
        self.assertEqual(self.user.add_category
                         ("Things I should do before I am 30 years old"),
                         "A category with this name already exists")

    def test_update_category(self):
        """ Tests updating a category """
        self.assertEqual(self.user.update_category(None, None), "None input")
        self.assertEqual(self.user.update_category(" ", "  "), "Blank input")
        self.assertEqual(self.user.update_category("notinthelistodcategories", "snewname"),
                         "Category not found")
        self.user.add_category("Things I should do before I am 90 years old")
        self.user.add_category("This is the current category name")
        self.assertEqual(self.user.update_category(
            "Things I should do before I am 80 years old",
            "Things I should do before I am 80 years old"), "No change, same name")
        self.assertEqual(self.user.update_category("This is the current category name",
                                                 "Things I should do before I am 90 years old"),
                         "No change, new name already in category")
        self.assertEqual(self.user.update_category("Things I should do before I am 90 years old",
                                                 "snewname"),
                         "Category name should than 2 characters")
        self.assertEqual(self.user.update_category
                         ("Things I should do before I am 90 years old",
                          "long name long name long name long name long name long name long name"),
                         "Category name should than 2 characters")
        self.assertEqual(self.user.update_category("Things I should do before I am 90 years old",
                                                 "Things I should do before I am 50 years old"),
                         "Category updated")


    def test_delete_category(self):
        """" Test deleting a category """
        self.assertEqual(self.user.delete_category(None), "None input")
        self.assertEqual(self.user.delete_category(" "), "Blank input")
        self.assertEqual(self.user.delete_category("This category does not exist"), "Category not found")
        self.user.add_category("Things I should do before I am 90 years old")
        self.assertEqual(self.user.delete_category("Things I should do before I am 90 years old"),
                         "Category deleted")

    def test_add_recipe(self):
        """ Tests adding a new recipe """
        category = Category('Test')
        self.assertEqual(category.add_recipe(None), "None input")
        self.assertEqual(category.add_recipe(" "), "Blank input")
        self.assertEqual(category.add_recipe("Get married"), "Recipe added")
        self.assertEqual(category.add_recipe("Get married"), "Recipe already exists")

    def test_update_description(self):
        """ Tests updating recipe description """
        category = Category('Test')
        self.assertEqual(category.update_description(None, None), "None input")
        self.assertEqual(category.update_description(" ", " "), "Blank input")
        self.assertEqual(category.update_description("Get married", "Get married"), "No changes")
        self.assertEqual(category.update_description("Get married", "Get schooled"), "Recipe not found")
        category.add_recipe("Get schooled")
        category.add_recipe("Travel Africa")
        self.assertEqual(category.update_description("Get schooled", "Travel Africa"),
                         "New description already in category")
        self.assertEqual(category.update_description("Get schooled", "Travel Europe"),
                         "Recipe updated")

    def test_update_status(self):
        """ Tests updating recipe status """
        category = Category('Test')
        self.assertEqual(category.update_status(None, None), "None input")
        self.assertEqual(category.update_status(" ", " "), "Blank input")
        self.assertEqual(category.update_status("Get married", "Pending"), "Recipe not found")
        category.add_recipe("Get schooled")
        category.add_recipe("Travel Africa")
        self.assertEqual(category.update_status("Get schooled", "The status"), "Invalid status")
        self.assertEqual(category.update_status("Travel Africa", "Done"),
                         "Recipe updated")

    def test_delete_recipe(self):
        """ Tests deleting an recipe from a category """
        category = Category('Test')
        self.assertEqual(category.delete_recipe(None), "None input")
        self.assertEqual(category.delete_recipe(" "), "Blank input")
        self.assertEqual(category.delete_recipe("Visit rwenzori mountain"), "Recipe not found")
        category.add_recipe("Get schooled")
        self.assertEqual(category.delete_recipe("Get schooled"), "Recipe deleted")

if __name__ == '__main__':
    unittest.main()