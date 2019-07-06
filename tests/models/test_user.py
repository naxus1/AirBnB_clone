import unittest
import uuid
from datetime import datetime, date, time
from models import *
from models.base_model import BaseModel


Class DefaultTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setUpClass classmethod")
    @classmethod
    def tearDownClass(self):
        print("tearDownClass classmethod")
    def setUp(self):
        self.model = User()
        self.model.save()
        # create instance to reply
    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")    
        
    def tearDown(self):
        # action before destroy
        pass


if __name__ == '__main__':
    unittest.main()
