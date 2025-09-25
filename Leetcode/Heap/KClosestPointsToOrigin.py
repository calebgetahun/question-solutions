from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = -(point[0]**2 + point[1]**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, point))

            else:
                heapq.heappushpop(max_heap, (dist, point))

        final = []
        for dist, point in max_heap:
            final.append(point)
        return final

if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(sol.kClosest(points, k))

# TC: O(NlogK)
# SC: O(N)
