# TODO: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def faststrStr(self, haystack: str, needle: str) -> int:
       return haystack.find(needle)
        
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n > len(haystack):
            return -1
        

        starting_idxs = [i for i in range(len(haystack)) if haystack[i] == needle[0]]
        needle_idx = 0
        # print(starting_idxs)
        for idx in starting_idxs:
            for j in range(idx, len(haystack)):
                if needle_idx == n:
                    break
                if haystack[j] == needle[needle_idx]:
                    needle_idx += 1
                else:
                    needle_idx = 0
                    break
            if needle_idx == n:
                break
            # print('idx =', idx, 'j =', j)

        if needle_idx == n:
            return idx
        else:
            return -1                
    

                
                
#haystack = "sabutsad", needle = "sad"

if __name__ == '__main__':
    sol = Solution()

    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))

    haystack = "sabutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))

    haystack = "leetcode"
    needle = "leeto"
    print(sol.strStr(haystack, needle))

    haystack = "sad"
    needle = "sadbut"
    print(sol.strStr(haystack, needle))

    haystack = "hello"
    needle = "ll"
    print(sol.strStr(haystack, needle))

    haystack = "mississippi"
    needle = "issip"
    print(sol.strStr(haystack, needle))
    
    haystack = "mississippi"
    needle = "pi"
    print(sol.strStr(haystack, needle))

    haystack = "ababababababc"
    needle = "abababc"
    print(sol.strStr(haystack, needle))