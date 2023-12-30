from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        #for i in range(len(height)):
        #    for j in range(len(height)):
        #        x = abs(i-j)
        #        y = min(height[i],height[j])
        #        if x * y > max_area:
        #            max_area = x * y

        #height_idx = sorted([(i, height[i]) for i in range(len(height))], key = lambda x, y : y)
        height_idx = sorted([(i, height[i]) for i in range(len(height))], key = lambda x: x[1])
        print(height_idx)

        for i in range(len(height_idx)):
            x = height_idx[i]
            index = x[0]
            area = max([abs(index - j[0]) for j in height_idx[i::]]) * x[1]
            print(f"x={x} area={area}")
            if area > max_area:
                max_area = area

        #for i in range(len(height)):
        #    dists = [abs(x - i) for x in range(len(height))]
        #    heights = [min(height[i],height[x]) for x in range(len(height))]
        #    areas = [dists[x] * heights[x] for x in range(len(height))]
        #    if max(areas) > max_area:
        #        max_area = max(areas)
        return max_area

