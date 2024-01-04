import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        with open("../data/default_arguments_input.txt") as f_i:
            input = [x.strip() for x in f_i.readlines()]

if __name__ == '__main__':
    unittest.main()
