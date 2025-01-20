from typing import List

class Solution:
    def sortColorsMultiPass(self, nums: List[int]) -> None:

        # 3 for loops, one for white, blue and red
        if len(nums) <= 1:
            return

        l = 0
        for curr in range(3):
            r = len(nums) - 1
            while l < r:
                if nums[l] == curr:
                    l += 1
                elif nums[r] == curr:
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    r -= 1
        
        return

    # AKA the dutch national flag algorithm from Dijkstra
    def sortColors(self, nums: List[int]) -> None:

        curr = p0 = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
            
        return
        
if __name__ == "__main__":
    sol = Solution()
    colors = [2,0,1,2,0,0,2,1,2,1,1]
    colors_2 = [2,0,1,2,0,0,2,1,2,1,1]
    sol.sortColors(colors)
    sol.sortColorsMultiPass(colors_2)
    print(colors)
    print(colors_2)

# TC: multi-pass: O(N), one-pass: O(N)
# SC: multi-pass: O(N), one-pass: O(1)