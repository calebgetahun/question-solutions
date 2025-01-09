import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        pileMax = max(piles)

        low, high = 1, pileMax
        while low < high:
            mid = low + ((high - low) // 2)
            if self.checkIfBananasDone(piles, h, mid):
                high = mid
            else:
                low = mid + 1

        return low

    def checkIfBananasDone(self, piles, h, k) -> bool:
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        return time <= h
        
if __name__ == "__main__":
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8

    print(sol.minEatingSpeed(piles, h))

# TC: O(nlogm) where n is the number of piles and m is the maximum of those piles
# SC: O(1)
