from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            
        return nums[low]
    
if __name__ == "__main__":
    sol = Solution()
    arr = [3,4,5,6,0,1,2]
    print(sol.findMin(arr))

# TC: O(logN)
# SC: O(1)
