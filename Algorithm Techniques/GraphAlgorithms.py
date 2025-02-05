from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
    
    def addVertex(self, a):
        if a not in self.graph:
            self.graph[a] = []
        else:
            print("vertex already exists, add an edge instead")
    
    def printAllVertices(self):
        for vertex in self.graph:
            print(f"vertex: {vertex}, edges: {self.graph[vertex]}")

    def dfsFromNode(self, curr_node, visited):
            if curr_node in visited:
                return
            visited.add(curr_node)
            print(f"{curr_node} -> ", end="")
            for node in self.graph[curr_node]:
                self.dfsFromNode(node, visited)

    def dfs(self):
        visited = set()
        print("DFS traversal: ", end="")
        for node in self.graph:
            if node not in visited:
                self.dfsFromNode(node, visited)
        
        print("\n")

    def bfs(self):
        visited = set()

        print("BFS traversal: ", end="")
        
        for node in self.graph:
            if node not in visited:
                q = deque([node])

                while q:
                    curr = q.popleft()
                    visited.add(curr)
                    print(f"{curr} -> ", end="")
                    for neighbor in self.graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

        print("\n")
    
    def checkConnectedComponents(self):
        comp_list = []
        visited = set()

        def dfs(curr_node, visited, component):
            if curr_node in visited:
                return
            
            visited.add(curr_node)
            component.append(curr_node)

            for node in self.graph[curr_node]:
                dfs(node, visited, component)

        for node in self.graph:
            if node not in visited:
                curr_comp = []
                dfs(node, visited, curr_comp)
                comp_list.append(curr_comp)

        return comp_list

    def shortestPath(self, a, b):
        #bfs from a until we find b, else nothin
        path = []
        parents = dict()
        visited = set()
        q = deque([a])
        while q:
            curr = q.popleft()
            visited.add(curr)
            for neighbor in self.graph[curr]:
                if neighbor not in visited:
                    parents[neighbor] = curr
                    q.append(neighbor)

                if neighbor == b:
                    val = neighbor
                    path.append(val)
                    while val in parents:
                        path.append(parents[val])
                        val = parents[val]

                    return " -> ".join(map(str, reversed(path)))
                    #stop, target found
        return "No path found"

g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(5, 6)

# g.printAllVertices()
# g.dfs()
# g.bfs()
# print(g.checkConnectedComponents())
# print(g.shortestPath(1,6))
