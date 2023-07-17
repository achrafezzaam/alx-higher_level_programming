import unittest
from models.base import Base

class TestBaseInstantiation(unittest.TestCase):
    def test_NoId(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_Id(self):
        b = Base(45)
        self.assertEqual(b.id, 45)

    def test_NullId(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_StrId(self):
        with self.assertRaises(TypeError):
            b = Base(12, 45)


if __name__ == '__main__':
    unittest.main()
