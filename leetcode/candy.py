from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        min_rating = min(ratings)
        candies = [None] * len(ratings)
        # pass 1
        for i in range(len(ratings)):
            if ratings[i] == min_rating:
                candies[i] = 1

        ratings_ordered = sorted(list(set(ratings)))
        print(candies)
        # pass n
        while not all(candies):
            for r in ratings_ordered:
                for i in range(len(ratings)):
                    prev_rating = min_rating
                    next_rating = min_rating
                    prev_candy = None
                    next_candy = None
                    if i != 0:
                        prev_rating = ratings[i - 1]
                        prev_candy = candies[i - 1]
                    if i != len(ratings) - 1:
                        next_rating = ratings[i + 1]
                        next_candy = candies[i + 1]
                    if not candies[i] and r == ratings[i]:
                        if ratings[i] <= prev_rating and ratings[i] <= next_rating:
                            candies[i] = 1
                        elif ratings[i] > prev_rating and ratings[i] <= next_rating:
                            candies[i] = (prev_candy or 1) + 1
                        elif ratings[i] <= prev_rating and ratings[i] > next_rating:
                            candies[i] = (next_candy or 1) + 1
                        elif ratings[i] > prev_rating and ratings[i] > next_rating:
                            candies[i] = max(next_candy or 1, prev_candy or 1) + 1
                print(candies)
        print(candies)
        return sum(candies)