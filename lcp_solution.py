
# TODO: Write a function to find the longest common prefix string amongst an array of strings.
from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        cp = ""
        match = True
        i = 0
        while i < len(first_string) and match:
            for s in strs:
                if i >= len(s):
                    match = False
                    break
                match = match and (first_string[i] == s[i])
            if match:
                cp += first_string[i]
            i += 1

        return cp

if __name__ == '__main__':
    sol = Solution()
    
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))
    print(sol.longestCommonPrefix([""]))
    print(sol.longestCommonPrefix(["racecar"]))
    print(sol.longestCommonPrefix(["ab", "a"]))
