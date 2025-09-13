import unittest
from calculator import add, subtract, multiply, divide
 
class TestCalculator(unittest.TestCase):
    """Test suite for the calculator functions."""
 
    def test_add(self):
        """Test the addition function."""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
 
    def test_subtract(self):
        """Test the subtraction function."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
 
    def test_multiply(self):
        """Test the multiplication function."""
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
 
    def test_divide(self):
        """Test the division function."""
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
 
    def test_divide_by_zero(self):
        """Test that division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10, 0)
 
if __name__ == '__main__':
    unittest.main()
