# TODO: Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#       If not, return the index where it would be if it were inserted in order in O(log n)

from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        match = False
        while (i < j) and (not match):
            mid_pt = (i + j) // 2
            if nums[mid_pt] == target:
                match = True
            elif nums[mid_pt] < target:
                i = mid_pt + 1 
            else:
                j = mid_pt - 1
            
        
        if match:
            return mid_pt
        else:
            if nums[i] < target:
                return i+1
            else:
                return i
                

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,6]
    target = 5
    print(sol.searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 2
    print(sol.searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 7
    print(sol.searchInsert(nums, target))

    nums = [-10**4]
    target = -10**4
    print(sol.searchInsert(nums, target))

    nums = [-10**4]
    target = 10**4
    print(sol.searchInsert(nums, target))
