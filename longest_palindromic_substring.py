#TASK: Given a string s, return the longest palindromic substring in s. 
#https://leetcode.com/problems/longest-palindromic-substring/

from random import randint, choice

class Solution:

    def expandOutward(self, s: str, left: int, right: int) -> str:
        """Helper function to find longest palindrome about a center character"""

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1: right]


    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 1:
            return s
        
        longest_palindrome = s[0]
        for i in range(n):
            #ODD length palindromes
            odd_palindrome = self.expandOutward(s, i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
        
            #EVEN length palindromes
            even_palindrome = self.expandOutward(s, i, i+1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
    
    #Naive O(n^3) version
    def isPalindrome(self, s: str) -> bool:
        
        flag = True
        n = len(s) - 1
        for i in range((n+1)//2):
            if s[i] != s[n-i]:
                flag = False
                break
        
        return flag

    def naiveLongestPalindrome(self, s: str) -> str:
        
        longest_palindrome = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i: j+1]
                is_palindrome = self.isPalindrome(sub_str)
                if (is_palindrome) and (len(sub_str) > len(longest_palindrome)):
                    longest_palindrome = sub_str
        
        return longest_palindrome
    



#TEST
s = Solution()
characters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)]

def test1(test_str: str):
    print('string:', test_str)
    lp1 = s.naiveLongestPalindrome(test_str)
    lp2 = s.longestPalindrome(test_str)
    print('naive:', lp1)
    print('efficient:', lp2)
    if len(lp1) != len(lp2):
        raise AssertionError("Error!: Longest Palindrom not returned")

def test2(n=1000):
    test_str = ''.join([choice(characters) for i in range(n)])
    lp1 = s.naiveLongestPalindrome(test_str)
    lp2 = s.longestPalindrome(test_str)
    print('naive:', lp1)
    print('efficient:', lp2)
    if len(lp1) != len(lp2):
        raise AssertionError("Error!: Longest Palindrom not returned")
    
def test3():
    while True:
        n = randint(1, 100)
        test_str = ''.join([choice(characters) for i in range(n)])
        lp1 = s.naiveLongestPalindrome(test_str)
        lp2 = s.longestPalindrome(test_str)
        assert len(lp1) == len(lp2)


if __name__ == '__main__':
    test1('babad')
    print()
    test1('cbbd')

    # test2(1000)

    # test3()

