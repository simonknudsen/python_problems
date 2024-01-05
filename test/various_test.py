import unittest
from hackerrank import various

class MyTestCase(unittest.TestCase):
    def test_python_time_delta(self):
        self.assertEqual(
            "25200",
            various.python_time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
        self.assertEqual(
            "88200",
            various.python_time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))


    """
    def test_python_time_delta_from_files(self):
        with open("../data/python_time_delta_input.txt") as f_i:
            with open("../data/python_time_delta_answers.txt") as f_a:
                input = [x.strip() for x in f_i.readlines()][1::]
                answers = [x.strip() for x in f_a.readlines()]
                for i, ans in enumerate(answers):
                    t1 = input[2 * i]
                    t2 = input[2 * i + 1]
                    print(f"t1={t1} t2={t2}")
                    self.assertEqual(ans,various.python_time_delta(t1,t2))
    """

    def test_piling_up(self):
        self.assertEqual("Yes", various.piling_up([4, 3, 2, 1, 3, 4]))
        self.assertEqual("No", various.piling_up([1, 3, 2]))
        self.assertEqual("No", various.piling_up([1, 2, 3, 8, 7]))
        self.assertEqual("Yes", various.piling_up([1, 2, 3, 7, 8]))

if __name__ == '__main__':
    unittest.main()
