from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(curr, curr_set):

            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(n):
                if nums[i] not in curr_set:
                    curr.append(nums[i])
                    curr_set.add(nums[i])
                    backtrack(curr, curr_set)
                    curr.pop()
                    curr_set.remove(nums[i])
        
        backtrack([], set())
        
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
