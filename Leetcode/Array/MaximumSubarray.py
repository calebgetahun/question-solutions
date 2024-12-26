class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr_max = nums[0]
        temp_sum = nums[0]
        for i in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            curr_max = max(curr_max, temp_sum)

        return curr_max

if __name__ == "__main__":
    sol = Solution()
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    arr_2 = [-1,-2,-6,-4]
    print(sol.maxSubArray(arr))
    print(sol.maxSubArray(arr_2))

# TC: O(N)
# SC: O(1)
# Using the well known algorithm Kadane's algorithm which keeps a running sum of largest sum/window and updates if we encounter a value that could replace it as our new max while maintaining this max in another value