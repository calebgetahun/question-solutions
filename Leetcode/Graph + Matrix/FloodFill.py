from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m, n = len(image)-1, len(image[0])-1
        orig = image[sr][sc]
        q = deque()
        q.append((sr, sc))
        visited = {(sr, sc)}
        adj = [[-1,0], [1,0], [0, 1], [0, -1]]

        while len(q):
            curr = q.popleft()
            image[curr[0]][curr[1]] = color
            for pair in adj:
                row = pair[0] + curr[0]
                col = pair[1] + curr[1]
                if row >= 0 and row <= m and col >= 0 and col <= n and (row, col) not in visited:
                    if image[row][col] == orig:
                        visited.add((row, col))
                        q.append((row, col))
        
        return image

if __name__ == "__main__":
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, color = 1, 1, 2
    print(sol.floodFill(image, sr, sc, color))

# TC: O(m * n)
# SC: O(m * n) for visited set