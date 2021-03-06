# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
import unittest

def find_needle(haystack):
    for i, w in enumerate(haystack):
        if str(w).lower() == "needle":
            return f"found the needle at position {i}"

# best
# def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]), 'found the needle at position 3')
        self.assertEqual(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']), 'found the needle at position 5')
        self.assertEqual(find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]), 'found the needle at position 30')

if __name__ == '__main__':
    unittest.main()