import unittest
from challenges import calculator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        self.assertEqual(calculator(2, '/', 2), 1)
        self.assertEqual(calculator(10, '-', 7), 3)
        self.assertEqual(calculator(2, '*', 16), 32)
        self.assertEqual(calculator(2, '-', 2), 0)
        self.assertEqual(calculator(15, '+', 26), 41)
        self.assertEqual(calculator(2, '+', 2), 4)
        self.assertEqual(calculator(2, "/", 0), "Can't divide by 0!")


if __name__ == '__main__':
    unittest.main()
