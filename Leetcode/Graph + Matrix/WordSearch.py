from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, currIndex, visited):           
            if currIndex == len(word) - 1 and board[r][c] == word[currIndex]:
                return True

            for row, col in neighbors:
                new_r, new_c = row + r, col + c
                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == word[currIndex+1] and visited[new_r][new_c] != 1:
                    visited[new_r][new_c] = 1
                    if dfs(new_r, new_c, currIndex + 1, visited):
                        return True
                    else:
                        visited[new_r][new_c] = 0
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    if dfs(i, j, 0, visited):
                        return True

        return False

if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(sol.exist(board, word))

# TC: O(M*N*4^L) as we iterate through our entire board and dfs in 4 directions to check each letter of length L
# SC: O(M*N + L)