class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        final = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total + nums[i] == 0:
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                elif total + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
                
        return final

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))

# TC: O(N^2)
# SC: O(1) not counting the final output array of sums
