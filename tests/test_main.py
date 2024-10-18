import unittest
from src.main import check_password

class TestMain(unittest.TestCase):
    def test_check_password(self):
        with self.assertRaises(TypeError):
            check_password(0)
        self.assertEqual(check_password('Aabc123!@#'), False)
        self.assertEqual(check_password('Aabc123!@#$%'), True)
        self.assertEqual(check_password('ABcdefg12345678'), False)
        self.assertEqual(check_password('ABcdefg12345678!'), True)

if __name__ == '__main__':
    unittest.main()