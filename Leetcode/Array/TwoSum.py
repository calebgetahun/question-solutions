class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [seen[comp], i]
            seen[nums[i]] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [9,19,11,15]
    target = 24
    print(sol.twoSum(nums, target))
