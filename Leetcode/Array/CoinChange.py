from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, len(dp)):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])

        return dp[amount] if dp[amount] != amount + 1 else -1
    
if __name__ == "__main__":
    sol = Solution()
    coins = [1,3,4,5]
    amount = 7
    print(sol.coinChange(coins, amount))

# TC: O(N*M), where N is the amount given and M is the number of coins we have
# SC: O(N), where N is the amount given