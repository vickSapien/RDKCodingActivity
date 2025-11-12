import unittest
from Coding_Activity_2 import *

class Test_sortAndFindMedian(unittest.TestCase):

    def test_sortAndFindMedian(self):
        numbers = [4, 4, 5, 67, 647, 6, 4]
        self.assertEqual(sortAndFindMedian(numbers), 5)
    def test_insertionSort(self):
        numbers = [4, 4, 5, 67, 647, 6, 4]
        self.assertEqual(insertionSort(numbers), [4, 4, 4, 5, 6, 67, 647])

if __name__ == '__main__':
    unittest.main()
#4, 4, 4, 5, 6, 67, 647