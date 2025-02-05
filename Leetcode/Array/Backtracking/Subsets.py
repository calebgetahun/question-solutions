from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, index):
            res.append(curr[:])

            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        backtrack([], 0)

        return res

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3]
    print(sol.subsets(arr))

# TC: O(2^N)
# SC: O(2^N)