from typing import List

class Solution:
    def canPartitionBruteForce(self, nums: List[int]) -> bool:
        num_sum = sum(nums)

        if num_sum % 2 == 1 or len(nums) <= 1:
            return False
        
        target = num_sum // 2

        def canFindSubset(curr_sum, index):
            if curr_sum == target:
                return True
            
            if index >= len(nums) or curr_sum > target:
                return False
            
            without_index = canFindSubset(curr_sum, index + 1)
            with_index = canFindSubset(curr_sum+nums[index], index + 1)

            return without_index or with_index
        
        return canFindSubset(0, 0)

    # TC: O(2^N)
    # SC: O(N) recursive stack space

    def canPartitionMemo(self, nums):
        num_sum = sum(nums)
        
        if num_sum % 2 != 0:
            return False
        
        target = num_sum // 2
        memo = {}
    
        def canFindSubset(curr_sum, index):
            state = (curr_sum, index)
                        
            if state in memo:
                return memo[state]
                
            if curr_sum == target:
                return True
            if index >= len(nums) or curr_sum > target:
                return False
            
            include = canFindSubset(curr_sum + nums[index], index + 1)
            exclude = False
            if not include:
                exclude = canFindSubset(curr_sum, index + 1)
            
            result = include or exclude
            memo[state] = result
            return result
        
        return canFindSubset(0, 0)
    
    # TC: O(N * target), since we compute every state for each index which ranges from 0 to the target sum. If we ever go above the target sum, we exit by returning false
    # SC: O(N * target), as we are storing all of the above states in memory

    def canPartition1DDP(self, nums):
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False
        
        target = num_sum // 2
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[-1]
    
    # TC: O(N * target)
    # SC: O(target), to store our dp table

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 11, 9]
    print(sol.canPartitionMemo(nums) == sol.canPartitionBruteForce(nums) == sol.canPartition1DDP(nums))
