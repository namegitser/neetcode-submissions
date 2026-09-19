"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        added = set()

        def dfs(node):
            
            if not node:
                return None

            if node in graph:
                print(f'-already added{node.val}')
                return graph[node]

            if node not in graph:
                print(f'-adding{node.val}')
                clone = Node(node.val)
                graph[node] = clone
                
            for neighbor in node.neighbors:
                print(f'neighbor-{neighbor.val}')
                neighbor_clone = dfs(neighbor)
                clone.neighbors.append(neighbor_clone)


            return clone

        return dfs(node)




        
            

