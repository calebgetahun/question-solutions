class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_height = 0
        while right > left:
            curr = (right - left) * min(height[right], height[left])
            max_height = max(max_height, curr)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_height

if __name__ == "__main__":
    sol = Solution()
    water = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(water))

# TC: O(N)
# SC: O(1)