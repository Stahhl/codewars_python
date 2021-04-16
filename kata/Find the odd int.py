# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
import unittest

def find_it(seq):
    dict = {}
    for n in seq:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    for key in dict:
        if (dict[key] % 2 != 0):
            return key

# best
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

class test(unittest.TestCase):
    def tests(self):
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
        self.assertEqual(find_it([10]), 10);
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);

if __name__ == '__main__':
    unittest.main()