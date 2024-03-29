import unittest
import uuid
from datetime import datetime, date, time
from models import *


class Test_CityModel(unittest.TestCase):
    """
    Test city
    """

    def setUp(self):
        self.model = City()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")


if __name__ == "__main__":
    unittest.main()
