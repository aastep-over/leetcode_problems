
# TODO:Given a roman numeral, convert it to an integer.
# https://leetcode.com/problems/roman-to-integer/description/ù

class Solution:
    
    def romanToInt(self, s: str) -> int:
        roman_alfs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        int_rep = 0
        for i in range(len(s) - 1):
            curr_int = roman_alfs[s[i]]
            next_int = roman_alfs[s[i+1]]
            if curr_int < next_int:
                int_rep -= curr_int
            else:
                int_rep += curr_int

        int_rep += roman_alfs[s[-1]]

        return int_rep
            
        
    

if __name__ == '__main__':
    sol = Solution()
    s2 = sol.romanToInt('MMMCDXC')
    print('MMMCDXC =', s2)
    



