from typing import Optional
from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# bfs on the graph and create the new graph attachments to neighbors as we go
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = [node]

        start = Node(node.val)
        list_of_nodes = {node: start}

        while q:
            curr = q.pop(0)
            new_node = list_of_nodes[curr]
            for neighbor in curr.neighbors:
                if neighbor not in list_of_nodes:
                    list_of_nodes[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
            
                new_node.neighbors.append(list_of_nodes[neighbor])  

        return start
    
def create_adj_list_from_node(node):
    adj_list = defaultdict(list)
    seen = set()

    q = []
    q.append(clone)

    while q:
        curr = q.pop(0)
        # print([node.val for node in curr.neighbors])
        for neighbor in curr.neighbors:
            # print(curr.val, neighbor.val)
            if neighbor not in adj_list and neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)
            adj_list[curr].append(neighbor)
    
    return adj_list
    
if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors.append(node_2)
    node_1.neighbors.append(node_4)
    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)
    node_3.neighbors.append(node_2)
    node_3.neighbors.append(node_4)
    node_4.neighbors.append(node_1)
    node_4.neighbors.append(node_3)

    sol = Solution()
    #node_1 is our entry point
    clone = sol.cloneGraph(node_1)

    orig_list = create_adj_list_from_node(node_1)
    clone_list = create_adj_list_from_node(clone)

    print(orig_list == clone_list)

# TC: O(V + E) where V and E are the number of vertices and edges in our original graph
# SC: O(V) as we use our hashmap to store the vertices and their cloned counterparts