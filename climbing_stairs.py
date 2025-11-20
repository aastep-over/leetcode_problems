class Solution:
    def naiveclimbStairs(self, n: int) -> int:
        if (n == 1) or (n == 2):
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)


    def climbStairs(self, n: int) -> int:
        if (n == 1) or (n == 2):
            return n

        dpt = [1, 2] + [0 for i in range(n-2)]

        for i in range(2, n):
            dpt[i] = dpt[i-1] + dpt[i-2]

        return dpt[-1]


s = Solution()

print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))
print(s.climbStairs(40))