import unittest
from application.models import Recipe
class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.Recipe = Recipe("")


    def test_create_Recipe_instance(self):
        self.assertIsInstance(self.Recipe, Recipe, "Failed to create instance")