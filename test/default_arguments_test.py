import unittest
from hackerrank import default_arguments

class MyTestCase(unittest.TestCase):
    def test_hackerrank_provided_answers(self):
        #self.assertEqual(True, False)  # add assertion here
        with open("../data/default_arguments_input.txt") as f_i:
            input = [x.strip() for x in f_i.readlines()]
            print(input)
            result = default_arguments.process(input)
            result = [str(x) for x in result]
            with open("../data/default_arguments_answers.txt") as f_a:
                ans = [x.strip() for x in f_a.readlines()]
                print(result == ans)
                print(f"result={len(result)} ans={len(ans)}")
                for i in range(max(len(ans), len(ans))):
                    a = None
                    r = None
                    if i < len(ans):
                        a = ans[i]
                    if i < len(result):
                        r = result[i]
                    print(f"result={r} ans={a}")

if __name__ == '__main__':
    unittest.main()
