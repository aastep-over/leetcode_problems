#TASK: Given a string s, return the number of palindromic substrings in it.
#https://leetcode.com/problems/palindromic-substrings/description/

from random import randint, choice


class Solution:

    def expandOutward(self, s: str, left: int, right: int) -> int:
        
        p_count = 0
        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
            p_count += 1
            left -= 1
            right += 1
        
        return p_count
    
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        odd_palindromes = 0
        even_palindromes = 0
        for i in range(len(s)):
            #ODD Palindromes
            odd_palindromes += self.expandOutward(s, i, i)

            #Even Palindromes
            even_palindromes += self.expandOutward(s, i, i+1)
        
        total_palindromes = odd_palindromes + even_palindromes
        return total_palindromes


    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        flag = True
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                flag = False
                break
        
        return flag
    
    def naiveCountSubstring(self, s: str) -> int:
        n = len(s)
        p_count = 0
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s[i: j+1]):
                    p_count += 1
        
        return p_count


s = Solution()
characters = [chr(i) for i in range(97, 123)]
def test1(test_str: str):
    print(test_str)
    n1 = s.naiveCountSubstring(test_str)
    n2 = s.countSubstrings(test_str)
    print('naive:', n1)
    print('efficient:', n2)
    if n1 != n2:
        raise AssertionError('Wrong!!')

def test2(n=1000):
    test_str = ''.join([choice(characters) for i in range(n)])
    n1 = s.naiveCountSubstring(test_str)
    n2 = s.countSubstrings(test_str)
    print('naive:', n1)
    print('efficient:', n2)
    if n1 != n2:
        raise AssertionError('Wrong!!')

def test3():
    while True:
        n = randint(1, 100)
        test_str = ''.join([choice(characters) for i in range(n)])
        n1 = s.naiveCountSubstring(test_str)
        n2 = s.countSubstrings(test_str)
        assert n1 == n2


if __name__ == '__main__':
    # test1('abc')
    # print()
    # test1('aaa')

    # test2(1000)
    test3()





