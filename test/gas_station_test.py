import unittest
from leetcode import gas_station

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = gas_station.Solution()
        self.assertEqual(3, s.canCompleteCircuit([1, 2, 3, 4, 5],[3, 4, 5, 1, 2]))
        self.assertEqual(-1, s.canCompleteCircuit([2,3,4],[3,4,3]))

if __name__ == '__main__':
    unittest.main()
