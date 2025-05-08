import unittest
from utils import is_prime

class TestPrimeUtils(unittest.TestCase):
    def test_basic_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        

    def test_non_primes(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-1))

if __name__ == "__main__":
    unittest.main()