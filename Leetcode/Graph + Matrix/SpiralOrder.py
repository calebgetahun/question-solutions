from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        m, n = len(matrix), len(matrix[0])
    
        inw = 0
        while len(spiral) < (m * n):
            for i in range(inw, n-inw):
                spiral.append(matrix[inw][i])

            if len(spiral) == (m * n):
                return spiral

            for j in range(inw+1, m-inw):
                spiral.append(matrix[j][n-1-inw])

            if len(spiral) == (m * n):
                return spiral            
            
            for k in range(n-2-inw, inw-1, -1):
                spiral.append(matrix[m-1-inw][k])

            if len(spiral) == (m * n):
                return spiral
            
            for l in range(m-2-inw, inw, -1):
                spiral.append(matrix[l][inw])

            if len(spiral) == (m * n):
                return spiral

            inw += 1

        return spiral

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))

# TC: O(N * M), where N and M denote the dimensions of the matrix
# SC: O(1), not counting the output array