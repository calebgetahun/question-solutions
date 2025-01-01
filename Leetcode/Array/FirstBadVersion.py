# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(self, num, bad_num):
        if num < bad_num:
            return False
        else:
            return True
    def firstBadVersion(self, n: int, bad_num) -> int:
        low, high = 1, n
        while low < high:
            mid = low + ((high - low) // 2)
            if self.isBadVersion(mid, bad_num):
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    sol = Solution()
    num = 9

    first_bad_version = 4
    print(sol.firstBadVersion(5, first_bad_version))

# TC: O(logN), variation of binary search
# SC: O(1)