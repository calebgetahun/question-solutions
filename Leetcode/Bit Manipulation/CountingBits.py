from typing import List
import math

class Solution:
    def countBitsBruteForce(self, n: int) -> List[int]:
        def countOnes(num):
            count = int(math.log2(num) // 1)
            res = 0
            for i in range(count, -1, -1):
                if num - 2**i >= 0:
                    res += 1
                    num -= 2**i

            return res
        
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        ans = [0] * (n+1)
        ans[1] = 1
        for i in range(2, n+1):
            ans[i] = countOnes(i)

        return ans
    
    #TC: O(NlogN)
    #SC: O(1), not counting output array
    
    def countBitsOptimized(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        #linear time and single pass -> means we can build upon our solution starting from a "base case" of 0 and 1. 
        # 0, [1] [1, 2] [1, 2, 2, 3] [1, 2, 2, 3, 2, 3, 3, 4] [16 entries]

        # DP solution since we use the previous solutions to build upon the list.
        groups = int(math.log2(n+1) // 1) + 1

        res = [0] * (2**groups + 1)
        res[1] = 1
        
        for i in range(1, groups):
            halfway = 2**i + 2**(i-1)
            half = 2**(i-1)
            for j in range(2**i, halfway):
                res[j] = res[j - half]
                res[j+half] = res[j] + 1

        return res[:n+1]
    
    #TC: O(N)
    #SC: O(1), not counting output array

if __name__ == "__main__":
    sol = Solution()
    test_cases = [3, 8, 22]
    for case in test_cases:
        print(sol.countBitsBruteForce(case))
        print(sol.countBitsOptimized(case))
    
    