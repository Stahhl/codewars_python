# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
import unittest

def square_sum(numbers):
    result = [0]
    for n in numbers:
        result.append(n * n)
    return sum(result)

#best
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(square_sum([1,2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([-1,-2]), 5)
        self.assertEqual(square_sum([-1,0,1]), 2)

if __name__ == '__main__':
    unittest.main()