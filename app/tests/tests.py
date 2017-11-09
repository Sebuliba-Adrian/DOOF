import unittest
from app.src.modals import Category, Recipe, User


class TestCategoryMethods(unittest.TestCase):
    # None attribute
    def test_add_recipe_none(self):
        self.assertEqual(Category('Test').add_recipe(None), 'Input cannot be None')

    # Non Recipe attribute
    def test_add_recipe_non_Recipe(self):
        self.assertEqual(Category('Test').add_recipe('recipe'),
                         'Input should be of type Recipe')

    # Valid attribute
    def test_add_recipe_valid(self):
        self.assertEqual(Category('Test').add_recipe(Recipe('recipe')), True)


class TestUserMethods(unittest.TestCase):
    # None attribute
    def test_add_category_none(self):
        self.assertEqual(User('Adrian', 'morgan', 'man').add_category(
            None), 'Input cannot be None')

    # Non Recipe attribute
    def test_add_category_non_Category(self):
        self.assertEqual(User('Adrian', 'morgan', 'man').add_category(
            'category'), 'Input must be of type Category')

    # Valid attribute
    def test_add_category_valid(self):
        self.assertEqual(User('Adrian', 'morgan', 'man').add_category(
            Category('category')), True)


class TestRecipeMethods(unittest.TestCase):
    # Name should not be empty
    def test_set_name_empty(self):
        self.assertEqual(Recipe('IceTea').set_name(''), 'Name cannot be empty')

    # Name should not be None
    def test_set_name_none(self):
        self.assertEqual(Recipe('IceTea').set_name(None), 'Name cannot be None')

    # Valid name
    def test_set_name_valid(self):
        self.assertEqual(Recipe('IceTea').set_name('recipe'), True)

    # Valid status Pending Public
    def test_set_status_valid_pending(self):
        self.assertEqual(Recipe('IceTea').set_status('Public'), True)

    # Valid status Private
    def test_set_status_valid_done(self):
        self.assertEqual(Recipe('IceTea').set_status('Private'), True)

    # Invalid status
    def test_set_status_invalid(self):
        self.assertEqual(Recipe('IceTea').set_status('recipe'), 'Invalid status')


if __name__ == '__main__':
    unittest.main()
