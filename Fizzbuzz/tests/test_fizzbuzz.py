from main.fizzbuzz import fizz_buzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_3_in_FizzBuzz(self): 
        x = 3
        result = fizz_buzz(x)
        self.assertEqual(result, 'Fizz')
        # test 3 
    def test_5_in_FizzBuzz(self): 
        x = 5
        result = fizz_buzz(x)
        self.assertEqual(result, 'Buzz')
        # test 5
    def test_15_in_FizzBuzz(self):  
        x = 15
        result = fizz_buzz(x)
        self.assertEqual(result, 'FizzBuzz')
        # test 15    
    def test_18_in_FizzBuzz(self): 
        x = 18
        result = fizz_buzz(x)
        self.assertEqual(result, 'Fizz')
        # test 18   
    def test_20_in_FizzBuzz(self): 
        x = 20
        result = fizz_buzz(x)
        self.assertEqual(result, 'Buzz')
        # test 20
    