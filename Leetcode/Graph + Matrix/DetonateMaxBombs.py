from collections import defaultdict, deque
from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_graph = defaultdict(list)

        def bfs(start_node):
            q = deque()
            seen = set()
            q.append(start_node)

            while q:
                curr_bomb = q.popleft()
                seen.add(curr_bomb)

                for neighbor_bomb in bomb_graph[curr_bomb]:
                    if neighbor_bomb not in seen:
                        q.append(neighbor_bomb)
                        seen.add(neighbor_bomb)

            return len(seen)

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                distance = math.sqrt((bombs[j][1] - bombs[i][1])**2 + (bombs[j][0] - bombs[i][0])**2)
                
                #radius check, meaning j is in range of i and can be detonated
                if distance <= bombs[i][2]:
                    bomb_graph[i].append(j)
                
                if distance <= bombs[j][2]:
                    bomb_graph[j].append(i)
        
        #run bfs from each node
        max_bombs_detonated = 1
        for i in range(len(bombs)):
            max_bombs_detonated = max(max_bombs_detonated, bfs(i))

        return max_bombs_detonated
    
if __name__ == "__main__":
    sol = Solution()
    bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    print(sol.maximumDetonation(bombs) == 5)


# TC: O(N^2 + N(N + E)) => since E can be N^2 => O(N^3)
# SC: O(N + E) => O(N^2)
