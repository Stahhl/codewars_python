# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
from random import randint
import unittest

def alphabet_position(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.replace(" ", "").lower()
    arr = []
    for c in text:
        if c in letters:
            arr.append(str(letters.index(c) + 1))
    return " ".join(arr)

# best
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
        self.assertEqual(alphabet_position(str(randint(1, 9))), "")

if __name__ == '__main__':
    unittest.main()