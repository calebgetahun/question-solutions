from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = deque()
            q.append((i, j))
            grid[i][j] = 0
            area = 1
            while q:
                row, col = q.popleft()
                for row_n, col_n in neighbors:
                    new_row, new_col = row + row_n, col + col_n
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        area += 1
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 0
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        return maxArea

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))

# TC: O(M * N), where M and N are the dimensions of the grid
# SC: O(M * N)