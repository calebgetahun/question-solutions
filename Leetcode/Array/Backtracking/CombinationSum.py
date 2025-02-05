from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0].append([])

        for i in range(len(candidates)):
            for j in range(candidates[i], target+1):
                for combination in dp[j - candidates[i]]:
                    newList = combination[:]
                    newList.append(candidates[i])
                    dp[j].append(newList)

        return dp[target]

# TC: O(N ^ T)
# SC: O(T * 2^T)

    def combinationSumBackTracking(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr[:])
                return

            if curr_sum > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i, curr, curr_sum + candidates[i])
            curr.pop()
            dfs(i+1, curr, curr_sum)

        dfs(0, [], 0)

        return res
    
# TC: O(N ^ T)
# SC: O(T), since our recursion depth can take up T spaces 

if __name__ == "__main__":
    sol = Solution()
    arr, target = [2,3,6,7], 7

    print(sol.combinationSum(arr, target))
    print(sol.combinationSumBackTracking(arr, target))