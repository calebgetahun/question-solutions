from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited):
            if (r, c) in visited: 
                return

            visited.add((r, c))
            for n_r, n_c in neighbors:
                new_r, new_c = n_r + r, n_c + c
                if 0 <= new_r < m and 0 <= new_c < n and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)

        pac = set()
        atl = set()

        for i in range(n):
            dfs(0, i, pac)
            dfs(m-1, i, atl)

        for j in range(m):
            dfs(j, 0, pac)
            dfs(j, n-1, atl)

        return list(pac.intersection(atl))
    
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sol.pacificAtlantic(matrix))

# TC: O(N * M)
# SC: O(N * M)