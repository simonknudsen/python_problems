import unittest
from leetcode import container_with_most_water

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = container_with_most_water.Solution()
        self.assertEqual(49, s.maxArea([1,8,6,2,5,4,8,3,7]))
        self.assertEqual(1, s.maxArea([1,1]))
        self.assertEqual(4, s.maxArea([1, 2, 4, 3]))
        self.assertEqual(17, s.maxArea([2,3,4,5,18,17,6]))
        self.assertEqual(62, s.maxArea([6,4,3,1,4,6,99,62,1,2,6]))
        self.assertEqual(14608, s.maxArea([75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,
                                           101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,
                                           107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,
                                           120,179,37,63,94,47]))
        self.assertEqual(70, s.maxArea([0, 14, 6, 2, 10, 9, 4, 1, 10, 3]))
        self.assertEqual(15936, s.maxArea([177, 112, 74, 197, 90, 16, 4, 61, 103, 133, 198, 4, 121, 143, 55, 138, 47, 167, 165, 159, 93, 85, 53, 118, 127,
         171, 137, 65, 135, 45, 151, 64, 109, 25, 61, 152, 194, 65, 165, 97, 199, 163, 53, 72, 58, 108, 10, 105, 27,
         127, 64, 120, 164, 70, 190, 91, 41, 127, 109, 176, 172, 12, 193, 34, 38, 54, 138, 184, 120, 103, 33, 71, 66,
         86, 143, 125, 146, 105, 182, 173, 184, 199, 46, 148, 69, 36, 192, 110, 116, 53, 38, 40, 65, 31, 74, 103, 86,
         12, 39, 158]))
        self.assertEqual(92344, s.maxArea([59,15,23,55,30,47,61,74,86,25,42,40,21,0,87,79,45,42,0,47,61,93,69,1,42,93,2,92,
               15,97,38,26,64,14,33,95,61,94,21,48,20,15,88,41,67,28,72,12,22,73,60,35,66,81,88,61,74,90,53,41,87,44,67,4,58,0,
               51,19,47,72,19,19,87,60,12,55,88,84,19,10,57,31,46,76,12,34,37,39,77,42,80,16,86,0,20,96,0,71,16,99,95,87,18,83,
               47,30,90,87,15,9,50,24,41,48,0,5,82,89,44,11,84,77,28,22,77,0,19,29,24,87,29,19,74,47,54,74,78,44,13,45,54,63,69,
               47,11,22,52,46,63,49,57,47,26,37,22,3,90,41,32,14,28,13,85,54,61,40,80,39,84,94,36,90,9,5,37,21,27,42,19,43,91,
               28,42,69,66,64,72,8,5,56,22,85,70,7,92,83,99,72,74,84,18,10,26,28,15,64,49,95,58,20,38,49,48,80,70,66,97,42,74,
               2,50,48,40,72,8,32,55,7,56,81,43,75,91,70,3,59,86,4,54,44,24,44,45,72,76,15,91,73,9,65,28,11,66,68,84,74,52,91,
               81,8,73,77,35,16,47,38,75,33,94,29,77,70,25,74,95,54,89,86,27,98,3,7,61,69,75,45,43,79,89,77,88,62,54,23,30,53,
               14,6,86,60,87,15,31,13,89,78,19,30,64,46,80,67,6,41,37,33,87,32,13,28,9,53,42,15,76,72,68,42,78,6,55,66,21,38,
               31,62,16,50,92,32,48,72,51,54,14,40,88,53,73,1,81,34,54,23,2,82,95,70,77,74,29,84,92,50,22,23,13,38,73,5,22,21,
               78,73,28,44,14,16,97,39,69,78,73,75,1,75,9,48,98,38,74,27,22,66,29,44,89,94,34,14,0,56,88,30,30,16,26,96,32,23,
               35,53,1,60,28,54,88,37,2,86,76,77,65,50,95,46,95,85,41,29,51,93,38,39,75,20,55,1,16,87,24,3,40,77,63,20,31,51,
               58,85,89,86,14,6,36,10,5,83,47,46,65,98,39,55,38,66,75,93,67,43,33,91,46,25,68,61,46,51,65,56,36,6,94,3,65,30,
               13,70,66,60,68,31,58,59,86,48,25,13,42,92,56,75,35,54,0,3,67,46,6,32,54,94,91,48,97,56,31,10,78,97,22,46,80,81,
               5,18,81,82,31,23,74,39,50,9,45,51,64,12,49,70,97,4,16,40,4,14,48,35,76,26,32,99,24,64,32,29,82,13,11,65,37,37,
               56,87,98,1,90,62,66,92,84,63,48,0,3,52,66,3,88,43,29,72,42,53,37,74,34,71,87,97,37,76,86,93,16,84,95,58,46,13,2,
               82,28,50,34,31,55,1,86,95,44,15,67,38,20,56,12,54,28,51,3,17,80,89,10,48,73,57,6,71,70,9,53,98,11,39,81,66,40,
               67,13,36,34,33,74,54,89,86,60,69,90,63,86,22,52,49,70,77,6,76,48,29,37,53,79,49,93,61,67,33,80,81,70,15,66,96,
               21,55,35,82,77,25,97,63,47,50,12,17,27,71,45,28,0,83,81,79,84,74,92,51,60,25,84,82,92,2,78,13,58,13,47,87,90,45,
               50,89,47,15,58,26,86,4,54,38,39,36,69,23,62,14,26,22,39,63,56,31,65,35,96,75,0,96,62,43,41,65,32,88,32,91,14,70,
               47,69,8,38,57,29,13,71,43,91,94,82,54,2,65,72,37,14,99,90,10,14,33,51,79,65,91,63,8,5,33,7,26,93,45,35,22,10,7,
               66,2,53,48,8,55,66,80,45,80,32,35,90,46,20,93,77,37,84,40,98,41,25,5,68,18,3,3,40,13,10,6,15,15,7,76,71,73,56,
               16,5,88,3,47,86,23,40,63,60,24,3,58,65,80,16,85,98,19,41,39,84,3,97,52,19,4,28,90,29,36,58,34,77,61,33,63,36,73,
               27,48,49,82,59,67,63,75,52,61,46,93,52,82,49,50,34,68,6,62,10,36,51,68,22,28,81,56,91,17,81,70,65,31,5,24,98,68,
               51,50,81,49,96,86,32,45,36,66,65,42,81,75,30,32,95,5,60,76,61,3,45,42,74,10,25,79,87,23,99,90,74,32,40,22,18,72,
               19,6,90,84,1,71,11,31,55,6,36,67,34,49,71,79,44,97,41,69,28,28,93,27,71,19,11,11,93,30,83,12,88,73,48,89,97,59,
               73,52,65,9,20,51,11,91,30,55,40,71,76,68,52,21,47]))


if __name__ == '__main__':
    unittest.main()