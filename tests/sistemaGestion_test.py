import unittest
from sistemaGestionCafeteria import Bebida

# Test the inputStr function
# Tests for name
class TestCafeteria(unittest.TestCase):
    def test_name_correct(self):
        self.assertEqual(str(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44")), "CocaCola (2, 20, 30, 40, 44)")

    # Test for name with less than 2 characters
    def test_name_less_than_2_characters(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("A, 2, 20, 30, 40, 44")

    def test_name_2_characters(self):
        self.assertEqual(str(Bebida.inputStr("Ab, 2, 20, 30, 40, 44")), "Ab (2, 20, 30, 40, 44)")

    # Test for name with more than 15 characters
    def test_name_more_than_15_characters(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaColaCocaCola, 2, 20, 30, 40, 44")

    def test_name_15_characters(self):
        self.assertEqual(str(Bebida.inputStr("CocaColaCocaCol, 2, 20, 30, 40, 44")), "CocaColaCocaCol (2, 20, 30, 40, 44)")

    # Test for name with non-letter characters
    def test_name_with_non_letter_characters(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("Coca-Cola, 2, 20, 30, 40, 44")

    # Test for name with numbers
    def test_name_with_numbers(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola1, 2, 20, 30, 40, 44")

    # Test there is no name
    def test_no_name(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("2, 20, 30, 40, 44")

    def test_name_empty(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr(", 2, 20, 30, 40, 44")

    # Test for sizes
    # Correct tests
    def test_sizes_correct(self):
        self.assertEqual(str(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44")), "CocaCola (2, 20, 30, 40, 44)")

    # Test for sizes with more than 5 sizes
    def test_sizes_more_than_5(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44, 50")

    def test_sizes_5(self):
        self.assertEqual(str(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44")), "CocaCola (2, 20, 30, 40, 44)")

    # Test for sizes with non-ascending order
    def test_sizes_non_ascending_order(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, 20")

    def test_sizes_ascending_order(self):
        self.assertEqual(str(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 44")), "CocaCola (2, 20, 30, 40, 44)")

    def test_sizes_negative(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, -44")

    # Test for sizes with 0 values
    def test_sizes_0(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, 0")

    # Test for sizes greater than 48
    def test_sizes_greater48(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 50, 50")

    # Test for sizes with 48 as a value
    def test_sizes_48(self):
        self.assertEqual(str(Bebida.inputStr("CocaCola, 2, 20, 30, 40, 48")), "CocaCola (2, 20, 30, 40, 48)")

    # Test for sizes with repeated values
    def test_sizes_repeated(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, 40")

    # Test for sizes with null values
    def test_sizes_null(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola, 2, 20, 30, 40, None")

    def test_sizes_empty(self):
        with self.assertRaises(ValueError):
            Bebida.inputStr("CocaCola,  ")


