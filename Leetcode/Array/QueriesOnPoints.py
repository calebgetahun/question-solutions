from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        
        index = 0
        for x1, y1, r in queries:
            for x2, y2 in points:
                dist_to_center = ((x2-x1)**2 + (y2-y1)**2)**0.5
                if dist_to_center <= r:
                    answer[index] += 1
            index += 1
        
        return answer

if __name__ == "__main__":
    sol = Solution()
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]

    print(sol.countPoints(points, queries))

# TC: O(Q*N)
# SC: O(1), not including output array for query counts
