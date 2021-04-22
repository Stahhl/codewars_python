# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
import unittest

def high_and_low(numbers):
    arr = list(map(int, numbers.split(" ")))
    return f"{max(arr)} {min(arr)}"

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
        self.assertEqual(high_and_low("1 -1"), "1 -1");
        self.assertEqual(high_and_low("1 1"), "1 1");
        self.assertEqual(high_and_low("-1 -1"), "-1 -1");
        self.assertEqual(high_and_low("1 -1 0"), "1 -1");
        self.assertEqual(high_and_low("1 1 0"), "1 0");        
        self.assertEqual(high_and_low("-1 -1 0"), "0 -1");
        self.assertEqual(high_and_low("42"), "42 42");

if __name__ == '__main__':
    unittest.main()