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

# TC: O(N * 2^N), since we have N amount of work each step to copy each subset into our output array and 2^N total subsets
# SC: O(N), not counting output array, as we use curr to maintain an intermediate list