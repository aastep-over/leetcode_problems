
class Solution:
    def myAbs(self, x: int) -> int:
        if x < 0:
            return -x
        else:
            return x

    def naivemySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0

        short_diff, sqr = 10**10, 0
        for i in range(1, 257):
            q = x / i
            if (q >= 1) and (self.myAbs(q - i) < short_diff):
                short_diff, sqr = self.myAbs(q - i), i
        if (x / sqr) < sqr:
            return sqr - 1
        else:
            return sqr
    
    def mySqrt(self, x: int) -> int:

        # return 0 and 1
        if x <= 1:
            return x
        
        start = 1
        end = x
        
        while start < end:
            mid = (start + end) // 2
            m_sqr = mid ** 2
            next_m_sqr = (mid + 1) ** 2
            if (m_sqr == x) or (m_sqr < x and next_m_sqr > x):
                break
            if m_sqr > x:
                end = mid
            else:
                start = mid
        
        return mid
        

s = Solution()

print(s.mySqrt(8))
