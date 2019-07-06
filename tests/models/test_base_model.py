import unittest
import uuid
from datetime import datetime, date, time
from models import *


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2019, 7, 5, 1, 0, 0, 100000),
                     'updated_at': datetime(2019, 7, 5, 1, 0, 0, 100000),
                     'id': '12345678-0123-0123-0123-012345678901',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(self.model2.id,
                         '12345678-0123-0123-0123-012345678901')
        self.assertEqual(self.model2.created_at,
                         datetime(2019, 7, 6, 1, 0, 0, 100000))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_json(self):
        jsonified = self.model2.to_json()
        self.assertNotEqual(self.model2.__dict__, jsonified)
        self.assertNotIsInstance(jsonified["created_at"], datetime)
        self.assertNotIsInstance(jsonified["updated_at"], datetime)
        self.assertEqual(jsonified["created_at"], '2019-07-6 01:00:00.100000')
        self.assertTrue(hasattr(jsonified, "__class__"))
        self.assertEqual(jsonified["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
