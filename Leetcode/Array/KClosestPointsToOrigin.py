import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist_heap = []

        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            dist_heap.append((dist, point))

        heapq.heapify(dist_heap)
        final = []

        for _ in range(k):
            res = heapq.heappop(dist_heap)[1]
            final.append(res)
        return final

if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(sol.kClosest(points, k))

# TC: O(KlogN)
# SC: O(N)
