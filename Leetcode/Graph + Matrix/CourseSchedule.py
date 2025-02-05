from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        # if our directed graph contains a cycle, return false
        adj = [[] for _ in range(numCourses)]

        for j, i in prerequisites:
            adj[i].append(j)

        def dfs(u, color):
            color[u] = "GRAY"

            for v in adj[u]:
                if color[v] == "GRAY":
                    return True
                
                if color[v] == "WHITE" and dfs(v, color):
                    return True
            color[u] = "BLACK"
            return False

        color = ["WHITE"] * numCourses

        for i in range(numCourses):
            if color[i] == "WHITE":
                if dfs(i, color):
                    return False
            
        return True

if __name__ == "__main__":
    sol = Solution()
    prerequisites = [[1,0],[0,1]]
    print(sol.canFinish(2, prerequisites))

# TC: O(V + E)
# SC: O(V) for our color array
