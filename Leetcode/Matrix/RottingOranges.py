from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rottenOranges = []

        def bfs(row, col):
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            visited = {(row, col)}
            q = [(row, col)]
            while q:
                #queue enqueue method
                row, col = q.pop(0)
                for neighbor_row, neighbor_col in directions:
                    new_row, new_col = row + neighbor_row, col + neighbor_col
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] >= -1 and (new_row, new_col) not in visited:
                        if grid[row][col] == -2:
                            grid[new_row][new_col] = 1
                        else:
                            if grid[new_row][new_col] == -1:
                                grid[new_row][new_col] = grid[row][col] + 1
                            else:
                                grid[new_row][new_col] = min(grid[new_row][new_col], grid[row][col] + 1)
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                elif grid[i][j] == 2:
                    grid[i][j] = -2
                    rottenOranges.append((i, j))
                else:
                    grid[i][j] = float('-inf')

        # rottenOranges contains the coords of every rotten orange in our grid. We can run BFS from each grid and update the value to be the min it has seen
        for orange_row, orange_col in rottenOranges:
            bfs(orange_row, orange_col)

        curr_min = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    return -1
                curr_min = max(curr_min, grid[i][j])
            
        return curr_min
    
if __name__ == "__main__":
    sol = Solution()
    oranges = [[2,0,1,1,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,1,0,1,0,1],
                [2,0,1,0,1,0,1],
                [1,1,1,0,1,1,1]]
    print(sol.orangesRotting(oranges))
        
# TC: O(N*M)
# SC: O(N*M)