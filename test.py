import unittest
from main import suma, resta


class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1,1),2)

    def test_resta(self):
        self.assertEqual(resta(2,1),1)


if __name__ == "__main__":
    unittest.main()