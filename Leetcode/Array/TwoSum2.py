class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            curr_sum = numbers[high] + numbers[low]
            if curr_sum == target:
                return [low + 1, high + 1]
            elif curr_sum > target:
                high -= 1
            else:
                low += 1
        return [low, high]
        
if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums, target))
