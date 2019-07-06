import unittest
import uuid
from datetime import datetime, date, time
from models import *

class Test_ReviewModel(unittest.TestCase):
    """
    Test review
    """

    def setUp(self):
        self.model = Review()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")


if __name__ == "__main__":
    unittest.main()
