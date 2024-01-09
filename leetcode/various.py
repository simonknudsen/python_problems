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
    accum = list(accumulate(nums))
    accum_net = [x - target for x in accum]
    print(f"accumlate={accum}")
    print(f"accum_net={accum_net}")
    if accum[-1] < target:
        return 0
    last_neg = -1
    best_len = len(accum_net)
    #for i, v in enumerate(accum_net):
    #    if v > 0 and i - last_neg

    #for l in range(1, len(nums) + 1):
    #    for i in range(len(nums)):
    #        if sum(nums[i:i+l]) >= target:
    #            return l
    return 0

# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
def is_valid_sudoku(board: List[List[str]]) -> bool:
    nos = {}.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    b = [[int(x) if x != "." else 0 for x in y] for y in board]
    def valid_row(r):
        nos_check = nos.copy()
        for i in r:
            if i > 0:
                nos_check[i] += 1
        if max(nos_check.values()) > 1:
            return False
        return True
    def get_quadrant(x_start,y_start):
        r = []
        for i in range(x_start, x_start+3):
            for j in range(y_start, y_start+3):
                r.append(b[i][j])
        return r
    print(b)
    for i in range(len(board)):
        if not valid_row(b[i]):
            return False
        if not valid_row([r[i] for r in b]):
            return False
        for x in [0,3,6]:
            for y in [0,3,6]:
                if not valid_row(get_quadrant(x,y)):
                    return False
    return True

board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150
def is_isomorphic(s: str, t: str) -> bool:
    m = {}
    for i in range(len(s)):
        if not m.get(s[i]):
            m[s[i]] = t[i]
        elif m.get(s[i]) != t[i]:
            return False
    print(m)
    if len(set(m.values())) != len(m.values()):
        return False
    return True


if __name__ == '__main__':
    #print(remove_element([0,1,2,2,3,0,4,2],2))
    #print(remove_duplicates([1,1,2]))
    #print(remove_duplicates2([1,1,1,2,2,3]))
    #print(remove_duplicates2([0,0,1,1,1,1,2,3,3]))
    #print(best_time_to_buy_and_sell_stock_ii([7,1,5,3,6,4]))
    #print(best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
    #print(best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))
    #print(minimum_size_subarray_sum(7, [2,3,1,2,4,3]))
    #print(minimum_size_subarray_sum(4, [1, 4, 4]))
    #print(minimum_size_subarray_sum(11, [1,1,1,1,1,1,1,1]))
    #print(is_valid_sudoku(board1))
    #print(is_valid_sudoku(board2))
    print(is_isomorphic("badc","baba"))
