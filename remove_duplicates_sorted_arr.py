# TODO: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        check_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == check_element:
               continue
            else:
                nums[j] = nums[i]
                check_element = nums[i]
                j += 1

        # remove remaining elements
        for k in range(j, len(nums)):
            nums.pop()
        
        return j
    

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums_ori = nums.copy()
    k = sol.removeDuplicates(nums)
    print('k =', k, '\t', 'unique:', nums, '\t', 'original:', nums_ori)