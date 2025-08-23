from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        day_set = set(days)

        for i in range(1, len(dp)):
            if i in day_set:
                one = dp[i - 1] + costs[0]
                seven = dp[max(0, i - 7)] + costs[1]
                thirty = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(one, seven, thirty)
            else:
                dp[i] = dp[i - 1]

        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2, 7, 15]
    print(sol.mincostTickets(days, costs))