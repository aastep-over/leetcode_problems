
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Standardize len(a) >= len(b)
        if len(a) < len(b):
            temp = a
            a = b
            b = temp

        
        # Start summing
        summation = ""
        i = -1
        carry = 0
        while (i >= -len(b)):
            digit_sum = int(a[i]) + int(b[i]) + carry 
            q, r = digit_sum // 2, digit_sum % 2
            summation += str(r)
            carry = q
            i -= 1
        
        # complete sum with larger string
        while (i >= -len(a)):
            digit_sum = int(a[i]) + carry 
            q, r = digit_sum // 2, digit_sum % 2
            summation += str(r)
            carry = q
            i -= 1
        
        if carry == 1:
            summation += '1'
        
        return summation[::-1]


s = Solution()
a, b = "11", "1"
print(s.addBinary(a, b))

a, b = "1010", "1011"
print(s.addBinary(a, b))

a, b = "1111", "1111"
print(s.addBinary(a, b))
