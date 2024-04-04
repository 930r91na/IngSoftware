import unittest
from main import main
# Test to check if the biggest number is correct if it is at the end of the array
class TestMain(unittest.TestCase):
    # Test biggest at the beginning
    def test_biggest_at_beginning(self):
        numbers = [5, 4, 3, 2, 1]
        self.assertEqual(main(numbers), 5)
    
    # Test biggest in the middle
    def test_biggest_in_middle(self):
        numbers = [1, 2, 5, 3, 4]
        self.assertEqual(main(numbers), 5)

    # Test biggest at the end
    def test_biggest_at_end(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(main(numbers), 5)
    
    # Test empty array
    def test_empty_array(self):
        with self.assertRaises(ValueError):
            main([])
    
    # Test None array
    def test_none_array(self):
        with self.assertRaises(ValueError):
            main(None)
    
    # Test negative numbers
    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        self.assertEqual(main(numbers), -1)
    
    # Test mixed numbers
    def test_mixed_numbers(self):
        numbers = [-1, 2, -3, 4, -5]
        self.assertEqual(main(numbers), 4)
    
    # Test all the same numbers (Repeated numbers)
    def test_all_same_numbers(self):
        numbers = [1, 1, 1, 1, 1]
        self.assertEqual(main(numbers), 1)
    
    # Test null values in array
    def test_null_values(self):
        numbers = [1, 2, None, 4, 5]
        with self.assertRaises(ValueError):
            main(numbers)
    

    # Test floating point numbers not accepted
    def test_float_numbers(self):
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
        with self.assertRaises(ValueError):
            main(numbers)

    # Test non-descendant order the arrey
    def test_non_descendant_order(self):
        numbers = [1, 3, 2, 4, 5]
        self.assertEqual(main(numbers), 5)    

    #  Test descendant order the arrey
    def test_descendant_order(self):
        numbers = [5, 4, 3, 2, 1]
        self.assertEqual(main(numbers), 5)

    # Test a big array of numbers
    def test_big_array(self):
        numbers = [i for i in range(1000000)]
        self.assertEqual(main(numbers), 999999)

    # Test a big array of numbers with negative numbers
    def test_big_array_negative(self):
        numbers = [i for i in range(-1000000, 0)]
        self.assertEqual(main(numbers), -1)
    
    # Test entry with a non integer
    def test_non_integer_entry(self):
        numbers = [1, 2, 3, 4, 'a']
        with self.assertRaises(ValueError):
            main(numbers)
    
    
    

