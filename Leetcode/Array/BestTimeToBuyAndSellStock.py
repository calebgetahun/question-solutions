class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_prof = 0
        curr_buy = prices[0]
        for price in prices:
            if price < curr_buy:
                curr_buy = price
            max_prof = max(max_prof, price - curr_buy)
        return max_prof

if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    no_profit = [8,3,2,1]
    print(f"max profit is {sol.maxProfit(prices)}")
    print(f"max profit is {sol.maxProfit(no_profit)}")

# TC: O(N)
# SC: O(1)