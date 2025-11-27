# TODO: 
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0

        while left < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > max_vol:
                max_vol = vol
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol


    def maxAreaNaive(self, height: List[int]) -> int:
        max_vol = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                vol = min(height[i], height[j]) * (j - i)
                if vol > max_vol:
                    max_vol = vol

        return max_vol



if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
 
    assert  sol.maxArea(height) == expected

    # Test Case 2
    height = [1,1]
    expected = 1
 
    assert  sol.maxArea(height) == expected
