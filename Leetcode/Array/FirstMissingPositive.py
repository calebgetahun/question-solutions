class Solution:
    def firstMissingPositiveLinearSpace(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            if nums[0] < 1 or nums[0] > 1:
                return 1
            else:
                return 2
                
        seen = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in seen:
                return i
        return -1
    
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = [num for num in nums if num > 0]

        for num in nums:
            ind = abs(num) - 1
            if ind >= len(nums):
                continue
            if nums[ind] < 0:
                continue
            else:
                nums[ind] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,-1,1]

    print(sol.firstMissingPositiveLinearSpace(nums))
    print(sol.firstMissingPositive(nums))

# TC: O(N)
# SC: O(1), O(N) for not optimized linear space solution