
# TODO: Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'
# link: https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # check if s empty when p empty
        if not p:
            return not s
        
        # check if first characters match
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

        # recursive loop
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        
        
        

    def isMatch2(self, s, p):
        # Base case: if pattern is empty
        print(s, p)
        if not p:
            return not s
        
        # Check if the first character of s and p match
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
        
        # If there’s a `*` in the second position of the pattern
        if len(p) >= 2 and p[1] == '*':
            # Option 1: Skip `p[0]*` and try to match `s` with `p[2:]`
            # Option 2: Match one occurrence of `p[0]` if `first_match` is True
            return (self.isMatch2(s, p[2:]) or (first_match and self.isMatch2(s[1:], p))) # type: ignore
        else:
            # If there's no `*`, just check the next characters if `first_match` is True
            return first_match and self.isMatch2(s[1:], p[1:]) # type: ignore

if __name__ == '__main__':
    sol = Solution()
    # print(sol.isMatch("aa", "a"))
    # print(sol.isMatch("aa", "a*"))
    # print(sol.isMatch("ab", ".*"))
    # print(sol.isMatch("a", "."))
    # print(sol.isMatch("ab", "ab*"))
    # print(sol.isMatch("ab", "abc*"))
    # print(sol.isMatch("abc", "ab.*"))
    # print(sol.isMatch("aab", "c*a*b"))
    # print("s = ab", "p = .*c", sol.isMatch("ab", ".*c"))
    # print("s = aaa", "p = a*a", sol.isMatch("baaa", "b*aaa"))
    # print("s = abc", "p = .*c", sol.isMatch("abc", ".*c"))
    # print("s = aaa", "p = ab*a*c*a", sol.isMatch("aaa", "ab*a*c*a"))
    # print(sol.isMatch("abaac", ".ba*ac")) # type: ignore
    
    


    assert sol.isMatch("aa", "a") == False
    assert sol.isMatch("aa", "a*") == True
    assert sol.isMatch("ab", ".*") == True
    assert sol.isMatch("a", ".") == True
    assert sol.isMatch("ab", "ab*") == True
    assert sol.isMatch("ab", "abc*") == True
    assert sol.isMatch("abc", "ab.*") == True
    assert sol.isMatch("aab", "c*a*b") == True
    assert sol.isMatch("ab", ".*c") == False
    assert sol.isMatch("aaa", "a*a") == True
    assert sol.isMatch("abc", ".*c") == True # abcd | .*cd
    assert sol.isMatch('aaa', "a*aaa") == True
    assert sol.isMatch('baaa', "b*aaa") == True
    assert sol.isMatch('aa2', 'a*b') == False
    assert sol.isMatch("abaac", ".ba*ac") == True
