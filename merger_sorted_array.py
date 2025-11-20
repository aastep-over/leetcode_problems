from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        
        elif n == 0:
            pass

        elif nums1[m-1] <= nums2[0]:
            nums1[m:] = nums2
        
        else:
            j = 0
            for i in range(m+n):
                if (j < n) and (nums1[i] > nums2[j]):
                    temp = nums1[i:-1]
                    nums1[i] = nums2[j]
                    nums1[i+1:] = temp
                    j += 1
                print(nums1, j)
            print(j, n)
            if j < n:
                nums1[-(n-j): ] = nums2[-(n-j):]



if __name__ == '__main__':
    s = Solution()

    nums1 = [4,0,0,0,0,0]
    nums2 = [1,2,3,5,6]
    m = 1
    n = len(nums2)

    print(s.merge(nums1, m, nums2, n))
    print(nums1)