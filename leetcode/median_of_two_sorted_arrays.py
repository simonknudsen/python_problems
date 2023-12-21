from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        odd = (len1 + len2) % 2 != 0
        odd_index = (len1 + len2 - 1) / 2
        while i + j < odd_index:
            if nums1[i] > nums2[j] and j < (len2 - 1):
                j += 1
            elif i < (len1 - 1):
                i += 1
            else:
                break
        print(f"i={i} j={j}")
        print(f"odd {odd}")
        if odd:
            if nums1[i] > nums2[j]:
                return float(nums2[j])
            else:
                return float(nums1[i])
        else:
            return (nums1[i] + nums2[j]) / 2