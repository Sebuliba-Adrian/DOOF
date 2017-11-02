# app/test.py
import unittest
from app import app


class AppTests(unittest.TestCase):
    # setup and teardown  methods

    # The methods are executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # This is executed after each test
    def tearDown(self):
        pass




   
    # tests
    def test_landing_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'DOOF Recipes App', response.data)
        self.assertIn(b'Sign in', response.data)
        self.assertIn(b'Sign up', response.data)
      
    


if __name__ == "__main__":
    unittest.main()