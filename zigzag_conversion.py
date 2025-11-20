#TODO: Given a string s, write them in zigzag |/|/... and zigzag it joined line by line
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    # n rows => 2n-2 elements in a cycle, n-1 columns spanned by repeating cycle, num_cols = |s|/(2n-2) * (n-1)

    def convert(slef, s: str, numRows: int) -> str:

        #same row
        if numRows == 1:
            return s
        
        chr_idx = []   

        lenCycle = 2 * numRows - 2
        numCycles = (len(s) // lenCycle) + 1
        currCol = 0
        start_idx = 0
        stop_idx = min(lenCycle, len(s)) 
        for c in range(numCycles):
            
            i = 0 #row_idx
            j = currCol #col_idx
            count = 0
            for k in range(start_idx, stop_idx):
                if count >= numRows:
                    i -= 1
                    j += 1
                    chr_idx.append((s[k], [i-1, j]))
                    
                else:
                    chr_idx.append((s[k], [i, j]))
                    i += 1

                count += 1
            
            start_idx += lenCycle
            if c == numCycles - 2:
                stop_idx = min(stop_idx + lenCycle, len(s))
            else:
                stop_idx += lenCycle
            currCol += numRows - 1
        
        #arrange by row index
        chr_idx.sort(key=lambda x: x[-1])
        
        output = [chr[0] for chr in chr_idx]
        output = ''.join(output)
        
        return output

if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    sol = Solution()
    print(sol.convert(s, 4))
    print(sol.convert(s, 3))
    print(sol.convert("A", 4))

