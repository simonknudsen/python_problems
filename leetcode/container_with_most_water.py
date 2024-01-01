from typing import List
from statistics import mean
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        last_occur_idx_by_height = {}
        first_occur_idx_by_height = {}
        last_height = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > last_height:
                for h in range(last_height + 1, height[i] + 1):
                    last_occur_idx_by_height[h] = i
                last_height = height[i]
        last_height = 0
        for i in range(0, len(height)):
            if height[i] > last_height:
                for h in range(last_height + 1, height[i] + 1):
                    first_occur_idx_by_height[h] = i
                last_height = height[i]
        print(f"first_occur_idx_by_height={first_occur_idx_by_height}")
        print(f"last_occur_idx_by_height={last_occur_idx_by_height}")

        heights = first_occur_idx_by_height.keys()
        for h in heights:
            area = (last_occur_idx_by_height[h] - first_occur_idx_by_height[h]) * h
            if area > max_area:
                max_area = area
        return max_area

    def maxAreaLessOld(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        best_left = (0, height[0])
        best_right = (len(height)-1, height[len(height)-1])
        area = min(best_left[1], best_right[1]) * abs(best_right[0] - best_left[0])
        iter = 0
        rating = []
        for i in range(len(height)):
            j = len(height) - i
            rating.append(height[i] * (len(height) - min(i + 1, j))/2)
        print(f"rating={rating}")
        top_rating = sorted(sorted(range(len(rating)), key=lambda i: rating[i])[-10:])

        for i in [x for x in range(len(height) - 1) if x in top_rating]:
            #print(f"i={[x for x in range(len(height) - 1) if rating[x] >= 1]}")
            #print(f"i={i}")
            #print(f"j={[x for x in range(best_right[0], i, -1) if rating[x] >= 1]}")
            for j in [x for x in range(best_right[0], i, -1) if x in top_rating]:
                iter += 1
                #print(f"i area={min(height[i],best_right[1]) * abs(best_right[0] - i)}")

                if min(height[i],height[j]) * abs(j - i) >= area and height[i] and height[j]:
                    best_left = (i, height[i])
                    best_right = (j, height[j])
                area = min(best_left[1],best_right[1]) * abs(best_right[0] - best_left[0])
                if area > max_area:
                    max_area = area
                #print(f"best_left={best_left} best_right={best_right} area={area} i={i} j={j}")
        print(f"iter={iter}")
        return max_area

    def maxAreaOld(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        max_area = 0
        best_left = (0, height[0])
        best_right = (len(height)-1, height[len(height)-1])
        area = min(best_left[1], best_right[1]) * abs(best_right[0] - best_left[0])
        iter = 0
        for i in range(len(height) - 1):
            #if height[i] <= best_left[1]:
             #   continue
            print(f"i={i}")
            #if min(height[i], best_right[1]) * abs(best_right[0] - i) >= area:
            #    best_left = (i, height[i])
            #area = min(best_left[1], best_right[1]) * abs(best_right[0] - best_left[0])
            for j in range(best_right[0], i, -1):
                #if height[j] <= best_right[1]:
                #    continue
                iter += 1
            #if height[i] - best_left[1] >= i - best_left[0]:
            #    best_left = (i, height[i])
            #elif height[j] - best_right[1] >= best_right[0] - j:
            #    best_right = (j, height[j])
                print(f"i area={min(height[i],best_right[1]) * abs(best_right[0] - i)}")

                if min(height[i],height[j]) * abs(j - i) >= area and height[i] and height[j]:
                    best_left = (i, height[i])
                    best_right = (j, height[j])

                #print(f"j area={min(best_left[1],height[j]) * abs(j - best_left[0])}")
                #if min(best_left[1],height[j]) * abs(j - best_left[0]) >= area:
                #    best_right = (j, height[j])
                area = min(best_left[1],best_right[1]) * abs(best_right[0] - best_left[0])
                if area > max_area:
                    max_area = area
                print(f"best_left={best_left} best_right={best_right} area={area} i={i} j={j}")
        print(f"iter={iter}")
        return max_area