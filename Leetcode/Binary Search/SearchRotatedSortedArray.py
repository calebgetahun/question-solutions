from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # edge case
        if n == 1:
            return 0 if nums[0] == target else -1
        low, high = 0, len(nums) - 1

        # find pivot point
        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # set low and high to be at the start and end of the correct range to begin binary search
        if nums[low] <= target <= nums[n-1]:
            high = n - 1
        else:
            high = low - 1
            low = 0

        # perform binary search on the part of array that could contain our target
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # return -1 if no value has been found to match target
        return -1

    def searchOnePass(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right-left)//2)
            if nums[mid] == target:
                return mid

            if nums[left] > nums[right]:
                #rotated
                if nums[mid] > nums[right]:
                    #rotated on right side
                    if target > nums[mid] or target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1

                else:
                    #rotated on left side
                    if target < nums[mid] or target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1

            else:
                #not rotated
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

if __name__ == "__main__":
    sol = Solution()
    arr = [4,5,6,7,0,1,2]
    target = 3, 5, 0
    for val in target:
        print(sol.search(arr, val))
        print(sol.searchOnePass(arr, val))

# TC: O(logn)
# SC: O(1)