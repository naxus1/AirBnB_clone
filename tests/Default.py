import unittest

Class DefaultTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setUpClass classmethod")
    @classmethod
    def tearDownClass(self):
        print("tearDownClass classmethod")
    def setUp(self):
        # create instance to reply
        pass
    def tearDown(self):
        # action before destroy
        pass
    #self.assertEqual(Instance.property_value, value)
    #self.assertNotEqual(Instance.property_value, value)
    #self.assertNotEqual(Objecto.attr[idx], value)


if __name__ == '__main__':
    unittest.main()
