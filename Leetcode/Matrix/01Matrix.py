from collections import deque

class BruteForceSolution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        output = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                output[i][j] = self.bfs_to_zero(mat, i, j, m, n)
        
        return output
    
    def bfs_to_zero(self, mat, row, col, m, n):
        q = deque()
        seen = set()

        neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]

        if mat[row][col] == 0:
            return 0
        
        q.append((row, col, 1))
        while q:
            curr = q.popleft()
            seen.add(curr)
            for coord in neighbors:
                new_row, new_col = coord[0] + curr[0], coord[1] + curr[1]
                if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                    if mat[new_row][new_col] == 0:
                        return curr[2]
                    else:
                        q.append((new_row, new_col, curr[2] + 1))

if __name__ == "__main__":
    sol = BruteForceSolution()
    a = [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]
    
    b = [[0, 0, 0],
         [0, 1, 0],
         [1, 1, 1]]

    sol_matrix = sol.updateMatrix(b)
    for row in sol_matrix:
        print(row)