
# TODO: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

from typing import *


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == '__main__':
    sol = Solution()
    nums1 = [3,2,2,3]
    nums1_ori = nums1.copy()
    val1 = 3
    print("Number of elements not equal to", val1, 'in', nums1_ori, "=", sol.removeElement(nums1, val1))

    nums2 = [0,1,2,2,3,0,4,2]
    nums2_ori = nums2.copy()
    val2 = 2
    print("umber of elements not equal to", val2, 'in', nums2_ori, "=", sol.removeElement(nums2, val2), nums2)
