
#TODO: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# https://leetcode.com/problems/reverse-integer/description/

import sys

class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1

        # return 1 digit num
        if x < 10:
            return sign * x
    
        overFlow = False
        x_reversed = x % 10
        x_reversed_prev = x % 10
        i = 2
        while (x // (10 ** i)) > 0:
            curr_digit = (x % (10 ** i) - x % (10 ** (i-1))) // 10 ** (i-1)
            x_reversed = (x_reversed * 10 + curr_digit) % 2**31
            
            if x_reversed // 10 != x_reversed_prev:
                overFlow = True
                break
            x_reversed_prev = x_reversed    
            i += 1
        
        
        if not overFlow:
            # Obtain the first digit
            curr_digit = (x % (10 ** i) - x % (10 ** (i-1))) // 10 ** (i-1)
            x_reversed = (x_reversed * 10 + curr_digit) % 2**31
            
            if x_reversed // 10 != x_reversed_prev:
                overFlow = True
        
        if overFlow:
            return 0
        else:
            return sign * x_reversed

    def reverse1(self, x: int) -> int:
        if x < 0:
            x_str = str(x)[1:] # can not store as string because 1 chr requires 8 bits 
        else:
            x_str = str(x)

        n = len(x_str)
        num = int(x_str[-1])
        print('n =', n)
        for i in range(1, n-1):
            print('i =', i)
            next_num = int(x_str[n-1:n-2-i:-1])
            next_num %= 2 ** 31
            if next_num <= num: # if self.smallBinNextNum(num, next_num):
                num = 0
                # print('breaking')
                break
            num = next_num
            # print(num)
            # print()
        
        next_num = int(x_str[n-1:0:-1] + x_str[0])
        print('next num = ', next_num)
        next_num %= 2 ** 31
        print('last num =', num)
        if (next_num <= num):
            num = 0
        else:
            num = next_num
        if x < 0:
            num *= -1 

        return num
    
    def smallBinNextNum(self, num, next_num):
        bin_rep_next_num = bin(next_num)
        bin_rep_num = bin(num)
        bit_len_diff = len(bin_rep_next_num) - len(bin_rep_num)
        bin_rep_num = bin(num)[:2] + '0' * bit_len_diff + bin(num)[2:]
        print(next_num, num)
        print(bin_rep_next_num, bin_rep_num)

        return bin_rep_next_num <= bin_rep_num



if __name__ == '__main__':
    assert len(sys.argv) == 2, "Usage: python <x>"
    x = int(sys.argv[1])
    sol = Solution()
    print('input = ', x, 'output = ', sol.reverse(x))

    # type: ignore # 2^31 - 1 = 2147483647
    # 1111111119, reverse = 9111111111
    # 8463847412
