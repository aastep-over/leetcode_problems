# TODO: Given an integer numRows, return the first numRows of Pascal's triangle.
# Note: naiveGenerate performed slightly better than generator maybe because of slow computation of combinations function

from time import time
from typing import List

class Solution:
    def naiveGenerate(self, numRows: int) -> List[List[int]]:
        
        # Base Cases
        if numRows <= 0:
            return "numRows should be atleast 1!"
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        # Initialize Output
        rows = [[0 for i in range(row)] for row in range(1, numRows+1)]
        rows[0], rows[1] = [1], [1, 1]

        for i in range(2, numRows):
            curr_row = [1]
            # Sum two succssive elements in prev row
            for j in range(len(rows[i-1])-1):
                curr_row.append(rows[i-1][j] + rows[i-1][j+1])
            
            # Append last 1
            curr_row.append(1)
            rows[i] = curr_row
        
        return rows

    def generate(self, numRows: int) -> List[List[int]]:
        # Base Cases
        if numRows <= 0:
            return "numRows should be atleast 1!"
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        # Initialize Output
        rows = [[0 for i in range(row)] for row in range(1, numRows+1)]
        rows[0], rows[1] = [1], [1, 1]

        for j in range(2, numRows):
            rows[j] = [combination(j, k) for k in range(j+1)]
        
        return rows
    
def combination(n: int, r: int) -> int:
    num = 1
    for i in range(r):
        num *= (n-i)
    denom = 1
    for j in range(r):
        denom *= (r-j)
    
    return int(num // denom)



if __name__ == '__main__':
    sol = Solution()

    # Ex1.
    n = 5
    print(f"Example 1: \t input = {n}")
    s1 = time()
    print(sol.naiveGenerate(n), '\n')
    e1 = time()
    print('Runtime for naiveGenerator = {:3f}'.format(e1 - s1))
    s2 = time()
    print(sol.generate(n), '\n')
    e2 = time()
    print("Runtime for generator = {:3f}".format(e2-s2))
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------')

    # Ex2.
    n = 1
    print(f"Example 2: \t input = {n}")
    print(sol.naiveGenerate(n), '\n')
    print(sol.generate(n), '\n')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------')

    # Ex3.
    n = 10
    print(f"Example 3: \t input = {n}")
    s1 = time()
    print(sol.naiveGenerate(n), '\n')
    e1 = time()
    print('Runtime for naiveGenerator = {:3f}'.format(e1 - s1))
    s2 = time()
    print(sol.generate(n), '\n')
    e2 = time()
    print("Runtime for generator = {:3f}".format(e2-s2))

