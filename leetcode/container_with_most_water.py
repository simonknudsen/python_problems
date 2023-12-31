from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        #best_left = (0, height[0])
        #best_right = (len(height)-1, height[len(height)-1])
        #max_i = len(height) - 1
        best_left = (0, height[0])
        best_right = (len(height)-1, height[len(height)-1])
        area = min(best_left[1], best_right[1]) * abs(best_right[0] - best_left[0])
        for i in range(len(height) - 1):
            j = len(height) - 1 - i
            print(f"best_left={best_left} best_right={best_right} area={area} i={i} j={j}")
            #if height[i] - best_left[1] >= i - best_left[0]:
            #    best_left = (i, height[i])
            #elif height[j] - best_right[1] >= best_right[0] - j:
            #    best_right = (j, height[j])
            print(f"i area={min(height[i],best_right[1]) * abs(best_right[0] - i)}")
            if min(height[i],best_right[1]) * abs(best_right[0] - i) >= area:
                best_left = (i, height[i])
            area = min(best_left[1], best_right[1]) * abs(best_right[0] - best_left[0])
            print(f"j area={min(best_left[1],height[j]) * abs(j - best_left[0])}")
            if min(best_left[1],height[j]) * abs(j - best_left[0]) >= area:
                best_right = (j, height[j])
            area = min(best_left[1],best_right[1]) * abs(best_right[0] - best_left[0])
            if area > max_area:
                max_area = area
        return max_area

