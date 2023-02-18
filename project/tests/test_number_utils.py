from coe_number.number_utils import is_prime_list

import unittest

class TestPrimeNumber(unittest.TestCase):
    def test_give_1_2_3_is_primes(self): 
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        # test all prime numbers
    def test_give_4_5_6_have_one_primes(self): 
        prime_list = [4, 5, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
        # test one prime number
    def test_give_n2_5_7_is_prime(self): 
        prime_list = [-2,5,7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        # test one prime negative number
    def test_give_1_3_10_have_one_not_primes(self): 
        prime_list = [1,3,10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
        # test one not prime number
    def test_give_2_4_6_is_not_primes(self): 
        prime_list = [2,4,6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
        # test not prime number        
