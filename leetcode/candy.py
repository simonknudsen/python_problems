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
        # pass n
        while not all(candies) :
            prev_rating = min_rating
            next_rating = min_rating
            prev_candie = 1
            next_candie = 1
            for i in range(len(ratings)):
                if i != 0:
                    prev_rating = ratings[i - 1]
                    prev_candie = candies[i - 1] or 1
                if i != len(ratings) - 1:
                    next_rating = ratings[i + 1]
                    next_candie = candies[i + 1] or 1
                if not candies[i]:
                    if ratings[i] <= prev_rating and ratings[i] <= next_rating:
                        candies[i] = 1
                    elif ratings[i] > prev_rating and ratings[i] <= next_rating:
                        candies[i] = prev_candie + 1
                    elif ratings[i] <= prev_rating and ratings[i] > next_rating:
                        candies[i] = next_candie + 1
                    elif ratings[i] > prev_rating and ratings[i] > next_rating:
                        candies[i] = max(next_candie, prev_candie) + 1
        print(candies)
        return sum(candies)