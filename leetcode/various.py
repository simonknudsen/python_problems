from typing import List

# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
def remove_element(nums: List[int], val: int) -> int:
    val_indexes = []
    for i in range(len(nums)):
        if nums[i] == val:
            val_indexes.append(i)
    val_count = len(val_indexes)
    val_indexes.reverse()
    for i in val_indexes:
        nums.pop(i)
    print(f"nums={nums}")
    return val_count

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
def remove_duplicates(nums: List[int]) -> int:
    val_count = {}
    dup_indexes = []
    for i in range(len(nums)):
        x = nums[i]
        if not val_count.get(x):
            val_count[x] = 1
        else:
            val_count[x] += 1
        if val_count.get(x) and val_count.get(x) > 1:
            dup_indexes.append(i)
    dup_indexes.reverse()
    for i in dup_indexes:
        nums.pop(i)
    print(f"nums={nums}")
    return len(nums)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
def remove_duplicates2(nums: List[int]) -> int:
    val_count = {}
    dup_indexes = []
    for i in range(len(nums)):
        x = nums[i]
        if not val_count.get(x):
            val_count[x] = 1
        else:
            val_count[x] += 1
        if val_count.get(x) and val_count.get(x) > 2:
            dup_indexes.append(i)
    dup_indexes.reverse()
    for i in dup_indexes:
        nums.pop(i)
    print(f"nums={nums}")
    return len(nums)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
def best_time_to_buy_and_sell_stock_ii(prices: List[int]) -> int:
    delta = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
    return sum([x for x in delta if x > 0])

from itertools import accumulate

# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
def minimum_size_subarray_sum(target: int, nums: List[int]) -> int:
    print(f"accumlate={list(accumulate(nums))}")
    for l in range(1, len(nums) + 1):
        for i in range(len(nums)):
            if sum(nums[i:i+l]) >= target:
                return l
    return 0





if __name__ == '__main__':
    #print(remove_element([0,1,2,2,3,0,4,2],2))
    #print(remove_duplicates([1,1,2]))
    #print(remove_duplicates2([1,1,1,2,2,3]))
    #print(remove_duplicates2([0,0,1,1,1,1,2,3,3]))
    #print(best_time_to_buy_and_sell_stock_ii([7,1,5,3,6,4]))
    #print(best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
    #print(best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))
    print(minimum_size_subarray_sum(7, [2,3,1,2,4,3]))
    print(minimum_size_subarray_sum(4, [1, 4, 4]))
    print(minimum_size_subarray_sum(11, [1,1,1,1,1,1,1,1]))