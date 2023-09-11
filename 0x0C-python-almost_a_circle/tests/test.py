import unittest


def add_numbers(a, b):
    return a + b


class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)  # Check if the result is equal to 8

    def test_add_negative_numbers(self):
        result = add_numbers(-3, -7)
        self.assertEqual(result, -10)  # Check if the result is equal to -10

    def test_add_zero_to_number(self):
        result = add_numbers(9, 0)
        self.assertEqual(result, 9)  # Check if the result is equal to 9


if __name__ == '__main__':
    unittest.main()
