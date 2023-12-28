import unittest
from leetcode import candy

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = candy.Solution()
        print(s.candy([]))
        print(s.candy([1, 0, 2]))
        self.assertEqual(5,s.candy([1, 0, 2]))
        self.assertEqual(4, s.candy([1, 2, 2]))
        self.assertEqual(7, s.candy([1, 3, 2, 2, 1]))
        self.assertEqual(13, s.candy([1, 2, 87, 87, 87, 2, 1]))


        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
