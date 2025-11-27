
# TODO: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# link: https://leetcode.com/problems/string-to-integer-atoi/description/

# Description: 
# 1. Ignore leading whitespaces
# 2. Determine sign
# 3. Read int by skipping leading zeros, until a non-digit character or end of string
# 4. Output: signed int in [-2**31, 2**31], outside this range -> round to the nearest endpoint, no digit read -> return 0

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        # remove leading whitespaces
        s = s.lstrip()
        digits = [str(i) for i in range(10)]
        
        # determine the sign
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # read the digits
        i = 0
        digits_read = ""
        while (i < len(s)):
            if s[i] in digits:
                digits_read += s[i]
            else:
                break
            i += 1
        
        if len(digits_read) == 0:
            return 0
        
        # ensure 32bit signed int
        output = sign * int(digits_read)
        if output < -2**31:
            output_32b = -2**31
        elif output > 2**31 - 1:
            output_32b = 2**31 - 1
        else:
            output_32b = output  

        return output_32b
        

if __name__ == '__main__':
    sol = Solution()
    tests_file = "8_String to Integer_(atoi)\\test.txt"
    with open(tests_file, "r") as f:
        test_cases = f.readlines()
        test_cases = [test_cases[i][:-1] for i in range(len(test_cases))]

    for test in test_cases:
        test_case = test.split("||")
        test_input, test_output = test_case[0][1:-1], int(test_case[1])
        assert sol.myAtoi(test_input) == test_output
        
