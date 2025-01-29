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

    # TC: O(T * 2^T)
    # SC: O(T * 2^T)
