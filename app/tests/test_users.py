import unittest
 
from app import app
 
 
class UserTests(unittest.TestCase):
 
    
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
        self.assertEquals(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 

 
  
    # Ensure that the user is able to register
    def test_registration_page(self):
        pass

    # Ensure that the login page loads correctly
    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Sign up', response.data)   


 
 
if __name__ == "__main__":
    unittest.main()