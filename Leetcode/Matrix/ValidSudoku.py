from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row // 3, col // 3)]:
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])
        return True

if __name__ == "__main__":
    sol = Solution()
    sudoku = [["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

    print(sol.isValidSudoku(sudoku))

# TC: O(1) since the input size doesn't change
# SC: O(1) for the same reson above