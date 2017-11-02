import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Adrian", "adris", "secret")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_category_None(self):
        self.assertEqual(self.user.add_category(None), "None input")

    def test_add_category_blank_input(self):
        self.assertEqual(self.user.add_category(" "), "Blank input")

    def test_add_category_should_be_between10and60(self):
        self.assertEqual(self.user.add_category("shortname"),
                         "category name should be greater than 10 and less than 60 characters")

        self.assertEqual(self.user.add_category("long name long name long name long name long name long name long name"),
                         "category name should be greater than 10 and less than 60 characters")

    def test_add_category_bucket_added(self):
        self.assertEqual(self.user.add_category("Lunch"),
                         "category added")

    def test_add_category_name_already_exists(self):
        self.user.add_category("BreakFast")
        self.assertEqual(self.user.add_category
                         ("BreakFast"),
                         "An category with this name already exists")

    def test_update_category_None(self):
        self.assertEqual(self.user.update_category(None, None), "None input")

    def test_update_category_blank(self):
        self.assertEqual(self.user.update_category(" ", " "), "Blank input")

    def test_update_category_same_name(self):
        self.assertEqual(self.user.update_category("Beverage",
                                                    "Beverage"),
                         "No change, same name")

    def test_update_category_not_found(self):
        self.assertEqual(self.user.update_category("notinthelistofitemList", "snewname"),
                         "category not found")

    def test_update_category_no_change(self):
        self.user.add_category("")
        self.user.add_category("")

        self.assertEqual(self.user.update_category("Vegetable",
                                                    "smothie"),
                         "No change, new name already in category")

    def test_update_category_updated(self):
        self.user.add_category("Drinks and Beer")

        self.assertEqual(self.user.update_category("",
                                                    "Clothes and Dresses"),
                         "category updated")

    def test_delete_category_none(self):
        """" Test deleting a category """
        self.assertEqual(self.user.delete_category(None), "None input")

    def test_delete_category_blank(self):
        """" Test deleting a blank category """
        self.assertEqual(self.user.delete_category(" "), "Blank input")

    def test_delete_category_not_found(self):
        self.assertEqual(self.user.delete_category(
            "This category does not exist"), "category not found")

    def test_delete_category_deleted(self):
        self.user.add_category("This is an category")
        self.assertEqual(self.user.delete_category("This is an category"),
                         "category deleted")

