from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brute force: sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        # return nums[-1]
        for i in range(len(nums)):
            curr = abs(nums[i])
            if nums[curr-1] < 0:
                return curr
            nums[curr-1] *= -1

        return nums[-1]

if __name__ == "__main__":
    sol = Solution()
    arr = [1,3,4,2,2]
    print(sol.findDuplicate(arr))

# TC: O(N)
# SC: O(1)
