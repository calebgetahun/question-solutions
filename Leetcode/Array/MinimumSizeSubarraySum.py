class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:    
        l = 0
        curr_sum = 0
        min_sub = len(nums) + 1
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_sub = min(min_sub, r-l+1)
                curr_sum -= nums[l]
                l+=1
        
        if min_sub == (len(nums) + 1):
            return 0
        
        return min_sub
    
if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,1,2,4,3]
    target_one = 7
    arr_2 = [10,2,3]
    target_two = 6
    print(sol.minSubArrayLen(target_one, arr))
    print(sol.minSubArrayLen(target_two, arr_2))

# TC: O(N)
# SC: O(1)