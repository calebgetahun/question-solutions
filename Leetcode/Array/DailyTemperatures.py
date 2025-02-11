from typing import List

class Solution:
    def dailyTemperaturesBruteForce(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > curr:
                    res[i] = j-i
                    break
        
        return res
    
    # TC: O(N^2)
    # SC: O(1)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        first = (temperatures[-1], n-1)

        stack = [first]
        
        for i in range(len(temperatures)-2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if stack and temperatures[i] < stack[-1][0]:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
            
        return res

    # TC: O(N)
    # SC: O(N)

if __name__ == "__main__":
    sol = Solution()
    arr = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperaturesBruteForce(arr) == sol.dailyTemperatures(arr))
