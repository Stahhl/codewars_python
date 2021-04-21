# https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
import unittest

def maps(a):
    return list(x * 2 for x in a)

# best
# return [2 * x for x in a]

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(maps([1, 2, 3]), [2, 4, 6])
        self.assertEqual(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        self.assertEqual(maps([]), [])

if __name__ == '__main__':
    unittest.main()