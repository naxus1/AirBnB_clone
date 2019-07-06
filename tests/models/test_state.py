import unittest
import uuid
from datetime import datetime, date, time
from models import *


class Test_StateModel(unittest.TestCase):
    """
    Test state
    """

    def setUp(self):
        self.model = State()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
