import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    
    def test_fizz(self):
        result = fizzbuzz.Fizzbuzz([1,2,3], [7,4,8])
        self.assertEqual(result, fizz)

    def test_buzz(self):
        result = fizzbuzz.Fizzbuzz([1,2,3,4,5], [7,4,8,9,6])
        self.assertEqual(result, buzz)

    def test_fizzbuzz(self):
        result = fizzbuzz.Fizzbuzz([1,2,3,4,5,6,8,2,5,1], [7,4,8,9,6])
        self.assertEqual(result, fizzbuzz)
        

if __name__ =='__main__':
    unittest.main()