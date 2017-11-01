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
    def test_user_registeration(self):
        pass
 
 
if __name__ == "__main__":
    unittest.main()