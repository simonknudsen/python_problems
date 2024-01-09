import unittest

from leetcode import various

class VLTestCase(unittest.TestCase):
    def test_is_isomorphic(self):
        self.assertTrue(various.is_isomorphic("egg","add"))
        self.assertFalse(various.is_isomorphic("foo", "bar"))
        self.assertTrue(various.is_isomorphic("paper", "title"))
        self.assertFalse(various.is_isomorphic("badc", "baba"))


if __name__ == '__main__':
    unittest.main()
