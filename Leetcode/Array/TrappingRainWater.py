from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0           
        
        water = [[0, 0] for _ in range(n)]

        left_max = height[0]
        for i in range(1, n):
            water[i][0] = left_max
            if height[i] > left_max:
                left_max = height[i]

        right_max = height[n-1]
        for j in range(n-2, -1, -1):
            water[j][1] = right_max
            if height[j] > right_max:
                right_max = height[j]

        trapped_rain = 0
        for i in range(1, n-1):
            if water[i][0] and water[i][1]:
                water_trapped = min(water[i][0], water[i][1]) - height[i]
                if water_trapped > 0:
                    trapped_rain += water_trapped

        return trapped_rain
    
if __name__ == "__main__":
    sol = Solution()
    rain_water = [0,1,0,2,1,0,1,3,2,1,2]

    #expected answer = 6
    print(sol.trap(rain_water))

# TC: O(N)
# SC: O(N)
