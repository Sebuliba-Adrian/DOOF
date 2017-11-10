import unittest
from application.models import Category

def setUp(self):
        self.category = Category("")

def test_category_instantiation(self):
        self.assertIsInstance(self.category, Category,
                              "Failed to instantiate")

def test_add_recipe_none(self):
        self.assertEqual(self.category.add_recipe(None), "None input")

def test_add_recipe_blank(self):
        self.assertEqual(self.category.add_recipe(" "), "Blank input")

def test_add_recipe_added(self):
        self.assertEqual(self.category.add_recipe("mangoes"), "Recipe added")

def test_add_recipe_exists(self):
        self.category.add_recipe("mangoes")
        self.assertEqual(self.category.add_recipe(
            "mangoes"), "Recipe already exists")

def test_update_description_none(self):
        self.assertEqual(self.category.update_description(
            None, None), "None input")

def test_update_description_blank(self):
        self.assertEqual(self.category.update_description(
            " ", " "), "Blank input")

def test_update_description_no_changes(self):
        self.assertEqual(self.category.update_description(
            "Yello Mango", "Yello Mango"), "No changes")

def test_update_description_not_found(self):
        self.assertEqual(self.category.update_description(
            "Green mango", "Green Mango"), "Recipe not found")

def test_update_description_exists(self):
        self.category.add_recipe("Oranges")
        self.category.add_recipe("Apples")
        self.assertEqual(self.category.update_description("Oranges", "Apples"),
                         "New description already in Category")

def test_update_description_updated(self):
        self.category.add_recipe("Apples")
        self.assertEqual(self.category.update_description("Apples", "Berries"),
                         "Recipe updated")

def test_update_status_none(self):
        self.assertEqual(self.category.update_status(
            None, None), "None input")

def test_update_status_blank(self):
        self.assertEqual(self.category.update_status(" ", " "), "Blank input")

def test_update_status_not_found(self):
        self.assertEqual(self.category.update_status(
            "Stationary", "Pending"), "Recipe not found")

def test_update_status_invalid(self):
        self.category.add_recipe("Apples")
        self.category.add_recipe("Oranges")
        self.assertEqual(self.category.update_status(
            "Apples", "The status"), "Invalid status")

    # def test_update_status_recipe_updated(self):
    #     self.assertEqual(self.category.update_status("Ream", "Done"),
    #                      "Recipe updated")

def test_delete_recipe_none(self):

        self.assertEqual(self.category.delete_recipe(None), "None input")

def test_delete_recipe_blank(self):
        self.assertEqual(self.category.delete_recipe(" "), "Blank input")

def test_delete_recipe_not_found(self):
        self.assertEqual(self.category.delete_recipe(
            "Laptop"), "Recipe not found")

def test_delete_recipe(self):
        self.category.add_recipe("Book")
        self.assertEqual(self.category.delete_recipe("Book"), "Recipe deleted")

def test_get_recipe_count(self):

        pass

if __name__ == '__main__':
    unittest.main()       