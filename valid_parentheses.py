# TODO: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False
        
        # brackets = {'(': ')', '{': '}', '[': ']'}
        # if s[0] not in brackets.keys():
        #     return False

        # last_open = []
        # for i in range(len(s)):
        #     if s[i] in brackets.keys():
        #         last_open.append(s[i])
        #     elif (len(last_open) == 0) or (s[i] != brackets[last_open[-1]]):
        #         return False
        #     else:
        #         last_open.pop()
        # if len(last_open) != 0:
        #     return False
        # else:
        #     return True
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        if s[0] not in open_brackets:
            return False
        last_open = []
        for i in range(len(s)):
            if s[i] in open_brackets:
                last_open.append(s[i])
            elif (len(last_open) == 0) or (s[i] != close_brackets[self.return_idx(open_brackets, last_open[-1])]):
                return False
            else:
                last_open.pop()
        if len(last_open) != 0:
            return False
        else:
            return True

    def return_idx(self, l: list, q: str):
        i = 0
        while l[i] != q:
            i += 1
        return i
            

        
        
    

if __name__ == '__main__':
    sol = Solution()
    test_cases = ["()", "()[]{}", "(]", "([])", "((", "){", "(){}}{"]
    for s in test_cases:
        print(sol.isValid(s))
