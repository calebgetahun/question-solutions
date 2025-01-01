import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist_heap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(dist_heap, (dist, point))
        final = []
        for i in range(k):
            final.append(heapq.heappop(dist_heap)[1])
        return final

if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(sol.kClosest(points, k))

# TC: O(NlogK)
# SC: O(N)
