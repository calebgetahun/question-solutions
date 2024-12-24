class Solution:
    def binarySearchIterative(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    # TC: O(logN)
    # SC: O(1)
    
    def binarySearchRecursive(self, nums: list[int], target: int, low, high):
        mid = low + (high - low) // 2
        if low > high:
            return -1
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearchRecursive(nums, target, low, mid - 1)
        else:
            return self.binarySearchRecursive(nums, target, mid + 1, high)
    
    # TC: O(logN)
    # SC: O(logN)

if __name__ == "__main__":
    sol = Solution()
    arr = [1,3,5,6,7,9,13,16]
    target = 13

    print(sol.binarySearchRecursive(arr, target, 0, len(arr)-1))
    print(sol.binarySearchIterative(arr, target))


