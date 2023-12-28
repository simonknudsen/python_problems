from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)):
                x = abs(i-j)
                y = min(height[i],height[j])
                if x * y > max_area:
                    max_area = x * y
        return max_area

