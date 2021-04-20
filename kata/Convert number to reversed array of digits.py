#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
import unittest

def digitize(n):
    return list(map(int, str(n)[::-1]))

# best
# the same but wrapping it in "list" cuz newer python

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(digitize(35231),[1,3,2,5,3])
        self.assertEqual(digitize(23582357),[7,5,3,2,8,5,3,2])
        self.assertEqual(digitize(984764738),[8,3,7,4,6,7,4,8,9])
        self.assertEqual(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
        self.assertEqual(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

if __name__ == '__main__':
    unittest.main()