import unittest
import uuid
import os.path
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import *


class Test_FileStorage(unittest.TestCase):
    """
    Test FileStorage
    """

    def setUp(self):
        self.store = FileStorage()

        test_args = {'updated_at': datetime(2019, 7, 6, 1, 0, 0, 100000),
                     'id': '12345678-0123-0123-0123-012345678901',
                     'created_at': datetime(2019, 7, 5, 1, 0, 0, 100000)}
        self.model = BaseModel(test_args)

        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.store.all())

    def tearDown(self):
        import os
        if os.path.isfile("file.json"):
            os.remove('file.json')

    def test_all(self):
        self.assertEqual(len(self.store.all()), self.test_len)

    def test_new(self):
        self.assertEqual(len(self.store.all()), self.test_len)
        self.model.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_save(self):
        self.test_len = len(self.store.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.store.all()), self.test_len + 1)
        b = User()
        self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_reload(self):
        pass

if __name__ == "__main__":
    unittest.main()
