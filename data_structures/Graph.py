from typing import List
from collections import deque, defaultdict

class AdjacencyList:
	def __init__(self, numberOfNodes, isDirected=False):
		self.graph = defaultdict(list)
		self.isDirected = isDirected
		self.numberOfNodes = numberOfNodes

	def addEdge(self, start, end):
		self.graph[start].append(end)
		if not self.isDirected:
			self.graph[end].append(start)
			
	def printGraph(self):
		for i in range(self.numberOfNodes):
			print(f"{i}: {self.graph[i]}")

	def BFS(self, start):
		visited = set()

		q = deque()
		q.append(start)
		visited.add(start)
		
		while q:
			curr = q.popleft()
			print(f"{curr} -> ", end="")
			
			for neighbor in self.graph[curr]:
				if neighbor not in visited:
					q.append(neighbor)
					visited.add(neighbor)
		print()
		
	def DFS(self, start, visited=None):
		if not visited:
			visited = set()
			
		visited.add(start)
		print(f"{start} -> ", end="")
		
		for neighbor in self.graph[start]:
			if neighbor not in visited:
				self.DFS(neighbor, visited)
				
	def findShortestPath(self, start, end):
		visited = {start}
		q = deque()
		q.append((start, []))
		
		while q:
			curr, curr_path = q.popleft()
			if curr == end:
				return curr_path + [curr]
			
			for neighbor in self.graph[curr]:
				if neighbor not in visited:
					q.append((neighbor, curr_path + [curr]))
					visited.add(neighbor)
		return ["path doesn't exist"]
	
	def checkIfCycleExistsDirectedGraph(self):
		state = [0] * self.numberOfNodes
		
		def dfs(node):
			if state[node] == 1:
				return True
			if state[node] == 2:
				return False

			state[node] = 1
			
			for neighbor in self.graph[node]:
				if dfs(neighbor):
					return True
				
			state[node] = 2
			
			return False
		
		for i in range(self.numberOfNodes):
			if state[i] == 0:
				if dfs(i):
					return True
		
		return False
			
class AdjacencyMatrix:
	def __init__(self, numberOfNodes, isDirected=False):
		self.graph = [[0] * numberOfNodes for _ in range(numberOfNodes)]
		self.numberOfNodes = numberOfNodes
		self.isDirected = isDirected

	def addEdge(self, start, end):
		self.graph[start][end] = 1
		if not self.isDirected:
			self.graph[end][start] = 1

	def printGraph(self):
		for i in range(self.numberOfNodes):
			
			print(f"{i}: ", end="")
			for j in range(self.numberOfNodes):
				if self.graph[i][j] == 1:
					print(f"{j}, ", end="")
			print()
	
	def printMatrix(self):
		for i in range(self.numberOfNodes):
			print(self.graph[i])
			
class EgdeListGraph():
	def __init__(self):
		self.edges = []

	def addEdge(self, start, end, weight):
		self.edges.append((weight, start, end))
		
	def printEdges(self):
		for weight, start, end in self.edges:
			print(f"weight: {weight}, start: {start}, end: {end}")
	
def main():
	graph = AdjacencyList(5, True)
	graph.addEdge(0, 1)
	graph.addEdge(2, 0)
	graph.addEdge(3, 4)
	graph.addEdge(1, 2)
	graph.printGraph()
	
	matrix = AdjacencyMatrix(4)
	matrix.addEdge(0, 1)
	matrix.addEdge(3, 1)
	matrix.addEdge(0, 3)
	matrix.addEdge(2, 1)
	matrix.addEdge(2, 3)
	matrix.addEdge(0, 2)
	# matrix.printMatrix()
	
	edgeList = EgdeListGraph()
	edgeList.addEdge(0, 1, 7)
	edgeList.addEdge(3, 1, 5)
	edgeList.addEdge(0, 3, 4)
	edgeList.addEdge(2, 1, 6)
	edgeList.addEdge(2, 3, 2)
	edgeList.addEdge(0, 2, 1)
	# edgeList.printEdges()
	
	# graph.BFS(0)
	# graph.DFS(0)
	# print(graph.findShortestPath(0, 3))
	print(graph.checkIfCycleExistsDirectedGraph())
	
if __name__ == "__main__":
	main()